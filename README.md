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
```
---

## Database Models

### Company

Stores company information.

| Field | Type |
|------|------|
| name | CharField |
| cnpj | CharField |

---

### Position

Stores employee positions and salaries.

| Field | Type |
|------|------|
| title | CharField |
| salary | DecimalField |

---

### Employee

Stores employee information and relationships.

| Field | Type |
|------|------|
| name | CharField |
| age | IntegerField |
| cpf | CharField |
| company | ForeignKey |
| position | ForeignKey |

---

## CRUD Operations

The system supports complete CRUD operations for employees:

- Create employees
- Read employee data
- Update employee information
- Delete employees

## Author
Developed by Danyel França
