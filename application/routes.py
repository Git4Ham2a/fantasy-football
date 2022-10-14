# This is where your CREATE, READ, UPDATE AND DELETE functionality is going to go. 
from flask import render_template, url_for, redirect, request 
from application import app, db 
from application.models import Todos, Lists
from application.forms import TodoForm, ListForm

#READ 
@app.route('/', methods=['POST', 'GET'])
def index():
    todos = Todos.query.all()
    return render_template('index.html', title="To do List", todos=todos)

#CREATE 
@app.route('/add', methods=['POST','GET'])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        todos = Todos(
            tasks = form.tasks.data
        )
       
        db.session.add(todos)

        print("This is to test the submit")
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title="Add a new Task", form=form)

#UPDATE 
@app.route('/update/<int:tid>', methods=['GET', 'POST'])
def update(tid):
    form = TodoForm()
    tasks = Todos.query.get(tid)
    if form.validate_on_submit():
        tasks.tasks = form.tasks.data 
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.tasks.data = tasks.tasks
    return render_template('update.html', title="Update task", form=form)

#DELETE
@app.route('/delete/<int:tid>')
def delete(tid):
    tasks = Todos.query.get(tid)
    db.session.delete(tasks)
    db.session.commit()
    return redirect(url_for('index')) 