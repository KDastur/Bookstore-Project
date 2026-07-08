from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from catalog.models import Author, Book


class Command(BaseCommand):
    help = 'Loads sample authors and books for testing'

    def handle(self, *args, **kwargs):
        placeholder_content = ContentFile(b"This is a placeholder eBook file.")

        authors_data = [
            ("George", "Orwell", "English novelist known for dystopian fiction.", "1903-06-25", "British"),
            ("Jane", "Austen", "English novelist known for romantic fiction.", "1775-12-16", "British"),
            ("Mark", "Twain", "American writer and humorist.", "1835-11-30", "American"),
            ("Agatha", "Christie", "English writer known for detective novels.", "1890-09-15", "British"),
            ("F. Scott", "Fitzgerald", "American novelist of the Jazz Age.", "1896-09-24", "American"),
            ("Herman", "Melville", "American novelist and poet.", "1819-08-01", "American"),
            ("Charlotte", "Bronte", "English novelist and poet.", "1816-04-21", "British"),
            ("Leo", "Tolstoy", "Russian writer of realist fiction.", "1828-09-09", "Russian"),
            ("Mary", "Shelley", "English novelist, known for Gothic fiction.", "1797-08-30", "British"),
            ("H.G.", "Wells", "English writer known for science fiction.", "1866-09-21", "British"),
            ("Arthur Conan", "Doyle", "British writer, creator of detective fiction.", "1859-05-22", "British"),
            ("Bram", "Stoker", "Irish author known for Gothic horror.", "1847-11-08", "Irish"),
        ]

        authors = {}
        for first, last, bio, birth, nat in authors_data:
            author, _ = Author.objects.get_or_create(
                first_name=first, last_name=last,
                defaults={'bio': bio, 'birth_date': birth, 'nationality': nat}
            )
            authors[f"{first} {last}"] = author

        books_data = [
            ("1984", "Dystopian", 9.99, "A chilling vision of a totalitarian future.", 50, "Secker & Warburg", "1949-06-08", ["George Orwell"]),
            ("Animal Farm", "Satire", 7.99, "A satirical allegory of Soviet totalitarianism.", 30, "Secker & Warburg", "1945-08-17", ["George Orwell"]),
            ("Pride and Prejudice", "Romance", 6.99, "A witty exploration of love and social class.", 40, "T. Egerton", "1813-01-28", ["Jane Austen"]),
            ("Sense and Sensibility", "Romance", 6.49, "A story of two sisters navigating love and society.", 35, "T. Egerton", "1811-10-30", ["Jane Austen"]),
            ("Emma", "Romance", 7.49, "A comedic novel about matchmaking gone wrong.", 28, "John Murray", "1815-12-23", ["Jane Austen"]),
            ("Adventures of Huckleberry Finn", "Adventure", 8.49, "A boy's journey down the Mississippi River.", 25, "Chatto & Windus", "1884-12-10", ["Mark Twain"]),
            ("The Adventures of Tom Sawyer", "Adventure", 7.99, "A boy's mischievous adventures along the Mississippi.", 33, "American Publishing Company", "1876-12-01", ["Mark Twain"]),
            ("Murder on the Orient Express", "Mystery", 8.99, "A detective solves a murder aboard a snowbound train.", 45, "Collins Crime Club", "1934-01-01", ["Agatha Christie"]),
            ("And Then There Were None", "Mystery", 8.99, "Ten strangers are trapped on an island one by one.", 42, "Collins Crime Club", "1939-11-06", ["Agatha Christie"]),
            ("The Great Gatsby", "Classic", 9.49, "A tale of wealth, love, and tragedy in the Jazz Age.", 38, "Charles Scribner's Sons", "1925-04-10", ["F. Scott Fitzgerald"]),
            ("Tender Is the Night", "Classic", 8.79, "A story of an American couple's decline on the Riviera.", 20, "Charles Scribner's Sons", "1934-04-12", ["F. Scott Fitzgerald"]),
            ("Moby-Dick", "Adventure", 10.99, "A sailor's obsessive hunt for a great white whale.", 22, "Harper & Brothers", "1851-10-18", ["Herman Melville"]),
            ("Jane Eyre", "Romance", 8.29, "An orphan's journey to independence and love.", 36, "Smith, Elder & Co.", "1847-10-16", ["Charlotte Bronte"]),
            ("War and Peace", "Historical Fiction", 12.99, "An epic of Russian society during the Napoleonic era.", 18, "The Russian Messenger", "1869-01-01", ["Leo Tolstoy"]),
            ("Anna Karenina", "Historical Fiction", 11.99, "A tragic tale of love and society in Russia.", 24, "The Russian Messenger", "1877-01-01", ["Leo Tolstoy"]),
            ("Frankenstein", "Horror", 7.99, "A scientist creates a living being with tragic consequences.", 31, "Lackington, Hughes, Harding, Mavor & Jones", "1818-01-01", ["Mary Shelley"]),
            ("The War of the Worlds", "Science Fiction", 8.49, "Earth is invaded by Martians in this classic sci-fi tale.", 27, "William Heinemann", "1898-01-01", ["H.G. Wells"]),
            ("The Time Machine", "Science Fiction", 7.49, "An inventor travels far into the future of humanity.", 29, "William Heinemann", "1895-01-01", ["H.G. Wells"]),
            ("The Invisible Man", "Science Fiction", 7.29, "A scientist discovers how to become invisible, with dark results.", 19, "C. Arthur Pearson", "1897-01-01", ["H.G. Wells"]),
            ("A Study in Scarlet", "Mystery", 6.99, "The first appearance of detective Sherlock Holmes.", 41, "Ward Lock & Co.", "1887-01-01", ["Arthur Conan Doyle"]),
            ("The Hound of the Baskervilles", "Mystery", 8.49, "Sherlock Holmes investigates a legendary curse.", 39, "George Newnes Ltd", "1902-01-01", ["Arthur Conan Doyle"]),
            ("Dracula", "Horror", 8.99, "A vampire's terror is unleashed upon England.", 34, "Archibald Constable and Company", "1897-05-26", ["Bram Stoker"]),
            ("Down and Out in Paris and London", "Memoir", 7.49, "Orwell's account of poverty in two great cities.", 15, "Victor Gollancz Ltd", "1933-01-01", ["George Orwell"]),
            ("Persuasion", "Romance", 6.99, "A second chance at love after years of separation.", 26, "John Murray", "1817-12-20", ["Jane Austen"]),
            ("Mansfield Park", "Romance", 6.79, "A young woman navigates a wealthy but flawed family.", 21, "T. Egerton", "1814-05-09", ["Jane Austen"]),
            ("Life on the Mississippi", "Memoir", 7.99, "Twain's recollections of his life as a riverboat pilot.", 17, "James R. Osgood & Company", "1883-01-01", ["Mark Twain"]),
            ("The ABC Murders", "Mystery", 8.29, "A serial killer taunts Hercule Poirot with the alphabet.", 30, "Collins Crime Club", "1936-01-06", ["Agatha Christie"]),
            ("Billy Budd", "Classic", 6.49, "A sailor's tragic fate aboard a British warship.", 14, "Constable and Company", "1924-01-01", ["Herman Melville"]),
            ("The Professor", "Romance", 6.29, "A young man seeks his fortune as a teacher in Brussels.", 12, "Smith, Elder & Co.", "1857-01-01", ["Charlotte Bronte"]),
            ("The Kreutzer Sonata", "Classic", 6.99, "A man's jealousy and violence unravel his marriage.", 16, "The Russian Messenger", "1889-01-01", ["Leo Tolstoy"]),
        ]

        created_count = 0
        for title, genre, price, description, stock, publisher, pub_date, author_names in books_data:
            book, created = Book.objects.get_or_create(
                title=title,
                defaults={
                    'genre': genre,
                    'price': price,
                    'description': description,
                    'stock': stock,
                    'publisher': publisher,
                    'publication_date': pub_date,
                }
            )
            if created:
                book.file.save(f"{title}.txt", placeholder_content, save=True)
                book.authors.set([authors[name] for name in author_names])
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"Created: {title}"))
            else:
                self.stdout.write(f"Already exists: {title}")

        self.stdout.write(self.style.SUCCESS(f"\nDone. {created_count} new books created."))
        