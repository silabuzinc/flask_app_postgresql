Simple Flask Todo App using SQLAlchemy and SQLite database.

For styling [semantic-ui](https://semantic-ui.com/) is used.

### Setup

Create project with virtual environment

```console
mkdir myproject
cd myproject
python3 -m venv venv
```

Activate it

```console
venv\Scripts\activate
```

Install Flask

```console
pip install -r requirements.txt
```

Add .env with

```console
FLASK_APP=app.py
FLASK_DEBUG=1
SQLALCHEMY_DATABASE_URI=""postgresql://postgres:password@localhost:5432/flask""
```

Run the migrations

```console
flask db init
flask db migrate -m "Initial database"
flask db upgrade
```

Run the app

```console
flask run
```

Referenciado de [PatrickLoeber](https://github.com/patrickloeber/flask-todo)
# flask_app_postgresql
