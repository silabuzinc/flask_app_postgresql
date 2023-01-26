from flask import Blueprint, redirect, url_for, render_template, request
from src.models.todo import Todo
from src.db import db

put = Blueprint('put', __name__)

@put.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("get.home"))

@put.route("/update_form/<int:todo_id>")
def update_form(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()

    return render_template("form.html", data=todo)

@put.route("/update_todo/<int:todo_id>", methods=["POST"])
def update_todo(todo_id):
    title = request.form.get("title")
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.title = title
    db.session.commit()
    return redirect(url_for("get.home"))