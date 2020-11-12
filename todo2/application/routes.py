from flask import render_template, redirect, url_for, request

from application import db, app
from application.models import Todos
from application.forms import TodoForm

@app.route('/')
def index():
    all_reviews = Reviews.query.all()
    return render_template('index.html', all_reviews=all_reviews)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = ReviewsForm()
    if form.validate_on_submit():
        new_review = Reviews(task=form.task.data)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.route('/update/<int:reviews_id>', methods=['GET', 'POST'])
def update(reviews_id):
    form = ReviewsForm()
    review_to_update = Todos.query.get(todo_id)
    if form.validate_on_submit():
        todo_to_update.task = form.task.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.task.data = todo_to_update.task
    return render_template('update.html', form=form)

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo_to_delete = Todos.query.get(todo_id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('index'))
