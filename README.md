# Library Management System

This is a Django-based Library Management System that allows users to manage books, authors, categories, and borrowed books.

## Prerequisites

Before running the project, ensure you have the following installed on your system:

- Python 3.x
- pip (Python package manager)
- virtualenv (optional but recommended)

## Getting Started

Follow these steps to set up the project locally:

### 1. Clone the Repository

Clone the project from GitHub using the following command:

```bash
git clone https://github.com/AfshinMoussavi/Library-Management.git
cd Library-Management
```

2. Set Up a Virtual Environment (Optional but Recommended)
It's recommended to use a virtual environment to isolate your project dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install Dependencies
Install the necessary Python packages by running:

```bash
pip install -r requirements.txt
```

4. Apply Migrations
Before running the project, apply the migrations to create the necessary database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a Superuser
To access the Django admin interface, you need to create a superuser. Run the following command and follow the prompts to set up an admin user:

```bash
python manage.py createsuperuser
```

6. Load Initial Data
To populate the database with the initial data (e.g., books, authors, users), load the initial_data.json file:

```bash
python manage.py loaddata initial_data.json
```

7. Run the Development Server

```bash
python manage.py runserver
```
The application will be accessible at http://127.0.0.1:8000/.





