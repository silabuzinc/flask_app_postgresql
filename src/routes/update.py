from flask import Blueprint, redirect, url_for
from src.models.todo import Todo
from src.db import db

put = Blueprint('put', __name__)

@put.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("get.home"))