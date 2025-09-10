# Django Development Setup Guide 🚀

## 📋 **Prerequisites Checklist**

Before starting Django development, ensure you have:
- [ ] Python 3.9+ installed
- [ ] Basic understanding of Python fundamentals
- [ ] Text editor/IDE (VS Code recommended)
- [ ] Terminal/command line familiarity
- [ ] Git for version control

## 🔧 **Step-by-Step Setup**

### **1. Python Environment Setup**

```bash
# Check Python version
python --version
# Should show Python 3.9 or higher

# Check pip version
pip --version
```

### **2. Create Virtual Environment**

```bash
# Create project directory
mkdir django_projects
cd django_projects

# Create virtual environment
python -m venv django_env

# Activate virtual environment
# On macOS/Linux:
source django_env/bin/activate

# On Windows:
django_env\Scripts\activate

# You should see (django_env) in your terminal prompt
```

### **3. Install Required Packages**

```bash
# Upgrade pip
pip install --upgrade pip

# Install Django and essential packages
pip install Django==4.2.7
pip install djangorestframework==3.14.0
pip install python-decouple==3.8
pip install Pillow==10.0.1
pip install psycopg2-binary==2.9.7

# Development packages
pip install black==23.9.1
pip install flake8==6.1.0
pip install pytest-django==4.5.2

# Create requirements file
pip freeze > requirements.txt
```

### **4. Create Your First Django Project**

```bash
# Create Django project
django-admin startproject learning_platform
cd learning_platform

# Create your first app
python manage.py startapp courses

# Run initial migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see your Django app!

## 📁 **Project Structure Explanation**

```
learning_platform/           # Project root directory
├── manage.py                # Django's command-line utility
├── requirements.txt         # Python dependencies
├── .env                    # Environment variables (create this)
├── .gitignore             # Git ignore file (create this)
├── learning_platform/     # Project configuration directory
│   ├── __init__.py
│   ├── settings.py        # Main settings file
│   ├── urls.py           # URL routing
│   ├── wsgi.py           # WSGI configuration
│   └── asgi.py           # ASGI configuration
└── courses/              # Your first Django app
    ├── __init__.py
    ├── admin.py          # Admin interface configuration
    ├── apps.py           # App configuration
    ├── models.py         # Database models
    ├── views.py          # View functions/classes
    ├── urls.py           # App-specific URLs (create this)
    ├── tests.py          # Test cases
    └── migrations/       # Database migration files
        └── __init__.py
```

## ⚙️ **Essential Configuration Files**

### **1. Environment Variables (.env)**

Create a `.env` file in your project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

### **2. Updated settings.py**

```python
import os
from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',          # DRF
    'courses',                 # Your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'learning_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'learning_platform.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# REST Framework configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (User uploads)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

### **3. .gitignore file**

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
django_env/
.venv
pip-log.txt
pip-delete-this-directory.txt

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
media/

# Environment variables
.env
.env.local
.env.production

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

## 🎯 **Development Workflow**

### **Daily Development Routine:**

```bash
# 1. Activate virtual environment
source django_env/bin/activate

# 2. Pull latest changes (if working in team)
git pull origin main

# 3. Install any new dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start development server
python manage.py runserver

# 6. Code your features...

# 7. Create and run migrations for model changes
python manage.py makemigrations
python manage.py migrate

# 8. Run tests
python manage.py test

# 9. Commit your changes
git add .
git commit -m "Descriptive commit message"
git push origin your-branch
```

## 🧪 **Testing Your Setup**

Create a simple test to verify everything works:

### **courses/models.py**
```python
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

### **courses/admin.py**
```python
from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'created_at']
    list_filter = ['created_at', 'instructor']
    search_fields = ['title', 'description']
```

### **Run the test:**
```bash
# Create and apply migrations
python manage.py makemigrations courses
python manage.py migrate

# Run server and visit admin
python manage.py runserver
# Visit: http://127.0.0.1:8000/admin/
```

## 🚨 **Common Issues and Solutions**

### **Issue 1: Virtual Environment Not Working**
```bash
# Solution: Recreate virtual environment
deactivate
rm -rf django_env
python -m venv django_env
source django_env/bin/activate
pip install -r requirements.txt
```

### **Issue 2: ModuleNotFoundError**
```bash
# Solution: Make sure virtual environment is activated
source django_env/bin/activate
pip install -r requirements.txt
```

### **Issue 3: Migration Errors**
```bash
# Solution: Reset migrations (development only!)
rm -rf courses/migrations/
python manage.py makemigrations courses
python manage.py migrate
```

### **Issue 4: Static Files Not Loading**
```bash
# Solution: Collect static files
python manage.py collectstatic
```

## 📚 **Useful Django Commands Reference**

```bash
# Project and App Management
django-admin startproject project_name
python manage.py startapp app_name

# Database Operations
python manage.py makemigrations          # Create migration files
python manage.py migrate                 # Apply migrations
python manage.py sqlmigrate app_name 0001  # View SQL for migration
python manage.py showmigrations         # Show migration status

# User Management
python manage.py createsuperuser        # Create admin user
python manage.py changepassword username  # Change user password

# Development
python manage.py runserver              # Start development server
python manage.py runserver 8080         # Start on different port
python manage.py shell                  # Django shell
python manage.py dbshell               # Database shell

# Testing and Debugging
python manage.py test                   # Run tests
python manage.py test app_name          # Run tests for specific app
python manage.py check                  # Check for errors

# Static Files
python manage.py collectstatic          # Collect static files
python manage.py findstatic filename    # Find static file location

# Data Management
python manage.py loaddata fixture.json   # Load data from fixture
python manage.py dumpdata app_name       # Export data
```

## 🎉 **Next Steps**

Once your setup is complete:

1. **Week 8**: Build your first Django views and templates
2. **Week 9**: Create models and work with the database
3. **Week 10**: Add user authentication and forms
4. **Week 11**: Transform your Django app into a REST API

## 🆘 **Getting Help**

- **Django Documentation**: https://docs.djangoproject.com/
- **DRF Documentation**: https://www.django-rest-framework.org/
- **Stack Overflow**: Tag your questions with `django` and `python`
- **Django Discord**: https://discord.gg/xcRH6mN4fa

---

**Remember**: Take time to understand each step. Django has a learning curve, but once you grasp the concepts, you'll be building powerful web applications quickly!

Good luck with your Django journey! 🚀
