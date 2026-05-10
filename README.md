# Django_Registration_System_Using_SMTP

## Overview
A full-stack web application built with **Django** that allows users to register, create profiles, upload profile pictures, and receive confirmation emails via **SMTP (Gmail)**. This project demonstrates complete full-stack development with form handling, validation, image upload, and database integration.

## Features
- User Registration with secure authentication
- Secure password hashing
- Profile creation with profile picture upload
- Email confirmation using SMTP (Gmail)
- Form validation using Django ModelForms
- Clean and responsive UI using HTML & CSS

## Technologies Used
| Category   | Technology          |
|------------|---------------------|
| Language   | Python              |
| Framework  | Django              |
| Frontend   | HTML, CSS           |
| Database   | SQLite              |
| Email      | SMTP (Gmail)        |

## Project Structure

```
SMTP/
│
├── app/                    # Main app
│   ├── models.py           # User & Profile models
│   ├── views.py            # Registration, profile views
│   ├── forms.py            # Django ModelForms
│   ├── urls.py             # App URL routing
│   └── templates/          # HTML templates
│
├── static/                 # CSS and static files
├── media/                  # Uploaded profile pictures
├── manage.py
└── requirements.txt
```

## Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- pip
- Git

### Installation
1. **Clone the repository**
```bash
git clone https://github.com/your-username/django-registration-system.git
cd django-registration-system
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure SMTP Email settings**
In `settings.py`, update the following with your Gmail credentials:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

> **Note:** Use a Gmail **App Password** instead of your actual Gmail password. Enable 2FA on your Google account and generate an App Password from your Google Account settings.

5. **Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Run the development server**
```bash
python manage.py runserver
```

7. **Open in browser**
```
http://127.0.0.1:8000/
```

## Functionalities
- **Register** — Create a new user account with form validation
- **Login / Logout** — Secure session-based authentication
- **Profile Setup** — Add personal details and upload a profile picture
- **Email Confirmation** — Receive a confirmation email on successful registration
- **Database Storage** — All user data stored securely in SQLite

## Screenshots
> Add screenshots here after deployment
```
| Registration Page | Profile Page | Email Confirmation |
```

## Future Enhancements
- Password reset via email
- Social login (Google, GitHub OAuth)
- Admin dashboard for user management
- Deploy to cloud (Heroku / Railway / Render)

## Author
**Shavala Sundar Raju**
- GitHub: [@venkateshP-12](https://github.com/venkateshP-12)
- Email: shavalasundarraju@gmail.com
- LinkedIn: [Shavala Sundar Raju](https://linkedin.com/in/shavalasundarraju)

## License
This project is licensed under the **MIT License** — feel free to use and modify it.
