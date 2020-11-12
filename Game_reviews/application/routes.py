from flask import render_template, redirect, url_for, request

from application import db, app
from application.models import review, games
from application.forms import ReviewForm

@app.route('/')
def index():
    all_reviews = review.query.all()
    return render_template('index.html', all_reviews=all_reviews)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = review(review=form.task.data)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/update/<int:todo_id>', methods=['GET', 'POST'])
def update(review_id):
    form = ReviewForm()
    review_to_update = review.query.get(review_id)
    if form.validate_on_submit():
        review_to_update.task = form.task.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.task.data = todo_to_update.task
    return render_template('update.html', form=form)

@app.route('/delete/<int:todo_id>')
def delete(review_id):
    review_to_delete = review.query.get(review_id)
    db.session.delete(review_to_delete)
    db.session.commit()
    return redirect(url_for('index'))
