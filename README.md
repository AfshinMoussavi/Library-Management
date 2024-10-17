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
2. Set Up a Virtual Environment (Optional but Recommended)
It's recommended to use a virtual environment to isolate your project dependencies:

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
3. Install Dependencies
Install the necessary Python packages by running:

bash
Copy code
pip install -r requirements.txt
4. Apply Migrations
Before running the project, apply the migrations to create the necessary database tables:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
5. Create a Superuser
To access the Django admin interface, you need to create a superuser. Run the following command and follow the prompts to set up an admin user:

bash
Copy code
python manage.py createsuperuser
6. Load Initial Data
To populate the database with the initial data (e.g., books, authors, users), load the initial_data.json file:

bash
Copy code
python manage.py loaddata initial_data.json
7. Run the Development Server
Start the Django development server using the following command:

bash
Copy code
python manage.py runserver
The application will be accessible at http://127.0.0.1:8000/.

8. Accessing the Admin Panel
Once the server is running, you can log into the admin panel using the superuser credentials you created earlier:

Admin URL: http://127.0.0.1:8000/admin/
Username and password: Use the credentials you set when creating the superuser.
Project Structure
The main components of the project are organized as follows:

BooksManagement/: Contains the models for authors, books, categories, and borrowed books.
initial_data.json: Contains the initial data to be loaded into the database.
LibraryManagement/: The main Django project folder.
