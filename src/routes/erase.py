from flask import Blueprint, redirect, url_for
from src.models.todo import Todo
from src.db import db

erase = Blueprint('erase', __name__)


@erase.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("get.home"))