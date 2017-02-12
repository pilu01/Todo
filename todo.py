from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint

from model import Todo

main = Blueprint('todo',__name__)


@main.route('/')
def index():
    todo_list = Todo.query.all()
    return render_template('todo_index.html',todos=todo_list)


@main.route('/add',methods=['POST'])
def add():
    form = request.form
    t = Todo(form)
    t.save()
    return redirect(url_for('todo.index'))


@main.route('/delete/<int:todo_id>/')
def delete(todo_id):
    t = Todo.query.get(todo_id)
    t.delete()
    return redirect(url_for('.index'))
