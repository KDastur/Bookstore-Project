from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from catalog.models import Book
from .models import Order, OrderItem


@login_required
def checkout(request):
    if request.method != 'POST':
        return redirect('view_cart')

    cart = request.session.get('cart', {})
    if not cart:
        return redirect('view_cart')

    phone_number = request.POST.get('phone_number', '')

    # First pass: verify stock is still sufficient for everything in the cart
    books_to_email = []
    total = 0
    for book_id_str, quantity in cart.items():
        book = Book.objects.get(id=int(book_id_str))
        if quantity > book.stock:
            messages.error(request, f"Sorry, '{book.title}' only has {book.stock} left in stock. Please update your cart.")
            return redirect('view_cart')
        total += book.price * quantity
        books_to_email.append((book, quantity))

    order = Order.objects.create(
        user=request.user,
        status='paid',
        total_price=total,
        phone_number=phone_number,
    )

    for book, quantity in books_to_email:
        OrderItem.objects.create(
            order=order,
            book=book,
            quantity=quantity,
            price_at_purchase=book.price,
        )
        # reduce stock now that the order is confirmed
        book.stock -= quantity
        book.save()

    request.session['cart'] = {}

    email = EmailMessage(
        subject=f'Your Order #{order.id} - eBooks Attached',
        body=f'Thank you for your order! Your {len(books_to_email)} eBook(s) are attached.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[request.user.email],
    )
    for book, quantity in books_to_email:
        email.attach_file(book.file.path)
    email.send()

    return render(request, 'orders/order_success.html', {'order': order})