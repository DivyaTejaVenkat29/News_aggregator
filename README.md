# Personalized News Aggregator API

This project provides a simple API for accessing and searching articles from a CSV file. The system is built using Django and Django REST Framework (DRF) and offers three key endpoints:
- View all articles.
- View an article by its ID.
- Search articles based on a query.

Additionally, a simple HTML template allows users to interact with the endpoints in a browser.

## Features

- **View all articles**: Retrieve all articles in the system.
- **View article by ID**: Retrieve a specific article by its unique ID.
- **Search articles**: Search for articles based on a query entered by the user (in article title or summary).
- **HTML Template**: An interface to interact with the API via a web browser.


## Setup Instructions

Follow the steps below to set up the project on your local machine.

### Prerequisites

Ensure that the following software is installed on your system:

- Python 3.8 or higher
- pip (Python package installer)
- Virtualenv (optional but recommended for managing dependencies)

### 1. Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone https://github.com/yourusername/news-aggregator-api.git
cd news-aggregator-api
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

Create a virtual environment to manage the dependencies separately from your system Python environment:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Use pip to install the required dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not yet available, run the following command to install Django and Django REST Framework manually:

```bash
pip install django djangorestframework pandas
```

### 4. Set Up the Database (SQLite by Default)

Django uses SQLite as the default database. To set up the database:

```bash
python manage.py migrate
```

This will create the necessary tables in your database.

### 5. Create the CSV File

Ensure you have the `news_articles.csv` file that contains the article data (with columns such as `Title`, `Summary`, `Publication_Date`, `Source`, `URL`, and `Category`). Place this file in the following directory:

```bash
D:\News Aggregator\Categorization\
```

If you're using a different path, you can update the file path in the `views.py` file accordingly.

### 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will now be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 7. Access the Endpoints

- **View All Articles**: Go to [http://127.0.0.1:8000/articles/](http://127.0.0.1:8000/articles/).
- **View Article by ID**: Go to [http://127.0.0.1:8000/articles/1/](http://127.0.0.1:8000/articles/1/) (replace `1` with any valid article ID).
- **Search Articles**: Go to [http://127.0.0.1:8000/search/?query=example](http://127.0.0.1:8000/search/?query=example) (replace `example` with your search query).

You can also access the user-friendly HTML interface at [http://127.0.0.1:8000/](http://127.0.0.1:8000/), which allows you to interact with these endpoints via buttons and forms.

---

## Directory Structure

```
news-aggregator-api/
│
├── manage.py                # Django's command-line utility for administrative tasks
├── templates
    ├──articles_search.html     # HTML template for interacting with the API
└── api/                # The main Django app containing views and logic
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py              # Contains URL routing
    ├── views.py             # Contains the views for handling API requests
```

---

## Endpoints

### 1. `/articles/`
- **Method**: `GET`
- **Description**: Retrieve all articles from the dataset.
- **Response**: JSON array of articles.

### 2. `/articles/<id>/`
- **Method**: `GET`
- **Description**: Retrieve a specific article by its ID.
- **Response**: JSON object of the article.

### 3. `/search/?query=`
- **Method**: `GET`
- **Description**: Search for articles based on a query string (matches in title or summary).
- **Response**: JSON array of search results.

---

## Template Usage

Once you run the server, you can open your browser and go to:

- **`/`**: The main page with buttons to interact with the three endpoints:
  - View all articles
  - View a specific article by ID
  - Search for articles

---

## Troubleshooting

### 1. Missing CSV File
Make sure the `news_articles.csv` file exists in the specified path (`D:\\News Aggregator\\Categorization\\news_articles.csv`). If not, you need to update the file path in the code.

### 2. Database Migrations
If you encounter any errors related to migrations, you can try running:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Permission Issues
If you encounter permission issues related to accessing files or ports, ensure that you have the necessary permissions or run the commands as an administrator.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thanks to Django and Django REST Framework for providing the tools to easily build this API.
- Thanks to pandas for its powerful data manipulation capabilities, which made handling the CSV file straightforward.
