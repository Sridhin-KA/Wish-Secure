# 💖 WishSecure

> **A private digital space for two people to preserve memories, celebrate special dates, and keep meaningful moments secure.**

WishSecure is a **Django-based private relationship/memory web application** designed for two people. It provides a secure and personalized space where users can store special memories, important dates, wishes, photos, and other meaningful moments in one place.

The project focuses on combining **privacy, security, personalization, and a romantic user experience**.

---

## ✨ Features

### 🔐 Secure Authentication

* User login system
* Protected pages using Django authentication
* Session-based authentication
* Private content accessible only to authenticated users

### ❤️ Special Dates

Keep track of meaningful dates such as:

* 💕 First Meeting
* 💍 Anniversary
* 🎂 Birthdays
* 🌹 First Date
* ✨ Other personal milestones

Each special date can contain additional information and personalized content.

### 📸 Memories

Create and preserve memorable moments with:

* Photos
* Titles
* Descriptions
* Dates
* Personal messages

### 💌 Wishes

A dedicated space for writing and storing personal wishes and messages.

### 🏠 Personalized Dashboard

A customized home page that brings important relationship information together in one place.

### 🔒 Privacy-Focused Design

WishSecure is designed around the idea that personal memories should remain private.

---

## 🛠️ Tech Stack

### Backend

* **Python**
* **Django**
* **Django ORM**

### Frontend

* **HTML5**
* **CSS3**
* **JavaScript**
* **Django Templates**

### Database

* **PostgreSQL**
* **Neon PostgreSQL** for cloud database hosting

### Development & Deployment

* Git
* GitHub
* Environment variables
* WSGI
* Cloud deployment

---

## 📂 Project Structure

```text
Wish-Secure/
│
├── manage.py
│
├── wish_secure/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── <app_name>/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── static/
│
├── media/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

```bash
cd Wish-Secure
```

### 2. Create a Virtual Environment

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DATABASE_URL=your-database-url
```

> ⚠️ Never commit your `.env` file or database credentials to GitHub.

### 5. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an Admin User

```bash
python manage.py createsuperuser
```

Follow the terminal instructions.

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🗄️ Database

WishSecure uses **PostgreSQL** as its primary database.

For production/cloud deployment, the project can use a hosted PostgreSQL database such as Neon.

Django communicates with the database through its ORM, allowing models to be managed using Python instead of writing SQL for every operation.

Example:

```python
class SpecialDate(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
```

---

## 🔐 Security

Security is an important part of WishSecure.

The project follows Django's built-in security mechanisms including:

* CSRF protection
* Authentication and authorization
* Password hashing
* Session management
* ORM-based database queries
* Environment-based secret configuration
* Protected views
* Secure production configuration

For production deployment, make sure to configure:

```python
DEBUG = False
```

and properly configure:

* `ALLOWED_HOSTS`
* `CSRF_TRUSTED_ORIGINS`
* HTTPS
* Secure cookies
* Secret keys
* Database credentials

---

## 🎨 User Experience

WishSecure is designed to be more than a standard CRUD application.

The interface aims to provide a:

> **Private • Personal • Simple • Romantic**

experience.

The application uses personalized pages and visual styling to make memories and important dates feel meaningful rather than simply displaying database records.

---

## 📌 Current Modules

| Module            | Purpose                            |
| ----------------- | ---------------------------------- |
| 🔐 Authentication | Secure user login                  |
| 🏠 Dashboard      | Personalized home page             |
| ❤️ Special Dates  | Store important relationship dates |
| 📸 Memories       | Preserve memorable moments         |
| 💌 Wishes         | Store personal wishes/messages     |

---

## 🔮 Future Improvements

Possible future features include:

* 📷 Advanced photo galleries
* 🎵 Background music
* ⏳ Relationship countdown timers
* 💌 Scheduled messages
* 🔔 Special-date reminders
* 🌙 Dark mode
* 📱 Improved mobile responsiveness
* 🗓️ Interactive relationship timeline
* 🔒 Two-factor authentication
* ☁️ Cloud media storage
* 📊 Memory statistics
* 💖 Personalized animations
* 🔐 End-to-end encryption for highly sensitive content

---

## 🧪 Development

Run Django's development checks:

```bash
python manage.py check
```

Run tests:

```bash
python manage.py test
```

Collect static files for production:

```bash
python manage.py collectstatic
```

---

## 🌍 Deployment

WishSecure can be deployed using platforms that support Python/Django applications.

Typical production architecture:

```text
             ┌─────────────────┐
             │     Browser     │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │  Django / WSGI  │
             └────────┬────────┘
                      │
             ┌────────▼────────┐
             │   PostgreSQL    │
             │     Database    │
             └─────────────────┘
```

---

## ⚠️ Environment Variables

Never push sensitive credentials to GitHub.

Your `.gitignore` should contain:

```gitignore
.env
venv/
__pycache__/
*.pyc
db.sqlite3
media/
staticfiles/
```

---

## 🤝 Contribution

WishSecure is primarily a personal project.

However, suggestions, improvements, and constructive feedback are welcome.

If you want to contribute:

```bash
git fork
git clone <repository-url>
git checkout -b feature/new-feature
```

Make your changes, commit them, and create a pull request.

---

## 📜 License

This project is currently intended for **personal use**.

If you plan to make WishSecure publicly available, add an appropriate open-source license such as MIT, Apache 2.0, or GPL depending on your requirements.

---

## 💖 Why WishSecure?

Most applications are built to solve business problems.

**WishSecure was built to preserve something personal.**

Instead of letting special dates, photographs, wishes, and memories get scattered across different applications, WishSecure brings them together into one private digital space.

> **Some memories are worth building an application for. ❤️**

---

### 👨‍💻 Developer

**Sidhu**

Built with ❤️ using **Python + Django + PostgreSQL**.
