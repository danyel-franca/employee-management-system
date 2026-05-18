# Employee Management System

A fullstack employee management system developed with Django, focused on employee organization, company management, and CRUD operations.

This project was built to strengthen backend development skills using Django, relational databases, and dynamic web applications.

---

## Overview

The Employee Management System allows users to manage employees, companies, and job positions through a clean and responsive interface.

The application includes full CRUD functionality integrated with a relational database using Django ORM.

---

## Features

- Employee registration
- Employee editing
- Employee deletion
- Employee listing
- Company management
- Position management
- Relational database integration
- Responsive interface with Bootstrap
- Django Admin panel

---

## Technologies Used

### Backend
- Python
- Django
- SQLite

### Frontend
- HTML5
- CSS3
- Bootstrap 5

---

## Project Structure

```bash
employee-management-system/
│
├── config/
│
├── employees/
│   ├── migrations/
│   ├── static/
│   │   └── employees/
│   │       └── style.css
│   │
│   ├── templates/
│   │   └── employees/
│   │       ├── home.html
│   │       └── update.html
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
