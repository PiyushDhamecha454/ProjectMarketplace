# ProjectMarketplace

## Overview
ProjectMarketplace is a web-based platform built using Django that allows users to browse, list, and manage various projects. The platform provides a structured marketplace for project collaboration and exchange.

## Features
- User authentication (Login, Logout, Registration)
- Create, edit, and manage project listings
- Image upload support for project previews
- Secure database management with Django ORM
- Responsive design for better user experience
- Admin panel for managing users and projects

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default, can be replaced with PostgreSQL or MySQL)
- **Virtual Environment:** Python 

## Installation
### 1. Clone the Repository
```bash
 git clone https://github.com/PiyushDhamecha454/ProjectMarketplace.git
 cd ProjectMarketplace
```

### 2. Create and Activate Virtual Environment
#### On Linux/macOS:
```bash
python3 -m venv Environment
source Environment/bin/activate
```
#### On Windows:
```bash
python -m venv Environment
Environment\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional for Admin Panel)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

## Directory Structure
```
ProjectMarketplace/
├── Environment/        # Virtual environment
├── Marketplace/        # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── conversation/       # Messaging module
├── core/               # Core application logic
├── dashboard/          # Admin dashboard
├── item/               # Project listing models
├── media/              # Uploaded images
├── manage.py           # Django CLI manager
└── db.sqlite3          # Database (default SQLite)
```

## Contributing
Feel free to contribute by forking the repository and submitting a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any queries, [reach out](https://github.com/PiyushDhamecha454).

___

**Note** : 
Set `DEBUG=False` in settings.py for Production