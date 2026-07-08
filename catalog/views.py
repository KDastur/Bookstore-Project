from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from django.db.models import Q

def book_list(request):
    query = request.GET.get('q', '')

    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(authors__first_name__icontains=query) | Q(authors__last_name__icontains=query)
        ).distinct()
    else:
        books = Book.objects.all()

    books = books.order_by('title')

    return render(request, 'catalog/book_list.html', {
        'books': books,
        'query': query,
    })

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'catalog/book_detail.html', {
        'book': book,
    })


@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart = request.session.get('cart', {})
    book_id_str = str(book_id)
    current_quantity = cart.get(book_id_str, 0)

    if current_quantity + 1 > book.stock:
        messages.error(request, f"Sorry, only {book.stock} copies of '{book.title}' are in stock.")
        return redirect('book_detail', book_id=book_id)

    cart[book_id_str] = current_quantity + 1
    request.session['cart'] = cart
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for book_id_str, quantity in cart.items():
        book = get_object_or_404(Book, id=int(book_id_str))
        subtotal = book.price * quantity
        total += subtotal
        items.append({'book': book, 'quantity': quantity, 'subtotal': subtotal})

    return render(request, 'catalog/cart.html', {
        'items': items,
        'total': total,
    })


@login_required
def remove_from_cart(request, book_id):
    cart = request.session.get('cart', {})
    cart.pop(str(book_id), None)
    request.session['cart'] = cart
    return redirect('view_cart')