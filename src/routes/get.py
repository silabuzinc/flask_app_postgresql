from flask import Blueprint, render_template
from src.models.todo import Todo

get = Blueprint('get', __name__)

@get.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)