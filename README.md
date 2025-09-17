# Django E-Commerce Application
A full-featured e-commerce web application built with Django, featuring user authentication, product catalog, shopping cart, order management, and payment processing.

Ready to be deployed as a docker container.

## Features

### User Management

User registration and authentication
User profiles and account management


### Product Catalog

Product listings with categories
Product search and filtering


### Shopping Experience

Shopping cart functionality
Guest checkout option


### Admin Panel

Product management
Order management
User management


### Tech Stack

Backend: Django 5.x, Django Framework

Database: PostgreSQL (SQLite for development)

Frontend: HTML, CSS, JavaScript, Tailwind CSS

Authentication: Django's built-in authentication

Containerization: Docker & Docker Compose


### Prerequisites

- Python 3.10+
- Docker and/or Docker Compose
- Git


## Local Development

### 1. Clone and setup virtual environment

```
   git clone https://github.com/aswin154/orgrange.git
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```
   cd avodha_market
   pip install -r requirements.txt
```

### 3. Environment variables

```
   touch .env
   # Edit .env files to add necessary environment variables
   # Optionally configure postgres database credentials
```

### 4. Initial setup
```
   python manage.py migrate
   python manage.py collectstatic  # This collects all static files into static_files directory
   python manage.py createsuperuser  # to create the admin account.
```

### 5. Run Development Server
```
   python manage.py runserver  # The development server is running on port 8000
```