# BookStore Project

A proof-of-concept e-commerce platform for books. Users can search by title/author, add books to
a cart, check out, and receive an email with the eBook file(s) attached.

## Tech Stack

- Python / Django 6.0.7
- SQLite
- python-decouple (for environment variables)
- Gmail SMTP (email delivery)

## Setup

1. **Clone and enter the project**
   ```bash
   git clone https://github.com/KDastur/Bookstore-Project.git
   cd Bookstore-Project
   ```

2. **Create a virtual environment and activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django python-decouple
   ```

4. **Create a `.env` file** in the project root:
   ```env
   SECRET_KEY=your-django-secret-key
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_gmail_app_password
   ```
   (Gmail requires an [App Password](https://support.google.com/accounts/answer/185833), not your regular password.)

5. **Run migrations and create an admin user**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Start the server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` for the site, or `/admin/` to add books.

## Notes

- No payment gateway — checkout marks orders as `paid` directly.
- eBook files are placeholders, attached to the confirmation email on purchase.
