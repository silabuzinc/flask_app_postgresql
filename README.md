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

Set environment variables in terminal

```console
set FLASK_APP=app.py
set FLASK_ENV=development
```

Run the migrations

```console
flask db init
flask db migrate -m "Initial database"
flask db upgrade
```

Run the app
```console
$ flask run
```

Referenciado de [PatrickLoeber](https://github.com/patrickloeber/flask-todo)
