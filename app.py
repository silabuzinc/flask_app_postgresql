from src import create_app
from src.db import db

app = create_app()

from src.models.todo import Todo

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
