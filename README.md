# Django To-Do App

This is a simple To-Do app built using Django.

## Prerequisites

Make sure you have the following installed:

- Python (3.x recommended)
- Django

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd todo
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Navigate to the project directory:

   ```bash
   cd todo
   ```

2. Apply migrations:

   ```bash
   python manage.py migrate
   ```

3. Run the development server:

   ```bash
   python manage.py runserver
   ```

4. Open your web browser and go to [http://127.0.0.1:8000/todo/](http://127.0.0.1:8000/todo/) to view the app.

## Structure

- `todo/`: Main Django project directory.
- `todoapp/`: Django app directory containing the To-Do app code.
- `templates/`: Directory for HTML templates.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django's command-line utility for administrative tasks.
- `requirements.txt`: File containing a list of Python dependencies.

## Contributing

Contributions are welcome! Please feel free to fork the repository and submit pull requests.
