from flask import render_template, redirect, url_for, request
from application import db, app
from application.models import Review, Games
from application.forms import ReviewForm

@app.route('/')
def index():
    all_reviews = Review.query.all()
    all_games = Games.query.all()
    return render_template('index.html', all_reviews=all_reviews, all_games=all_games)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = ReviewForm()
    all_games = Games.query.all()
    game_choices = []
    for game in all_games:
        game_choices.append((str(game.id), game.game))
    form.gameid.choices = game_choices
    if form.validate_on_submit():
        new_review = Review(review=form.review.data, game_id=form.gameid.data)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/update/<int:review_id>', methods=['GET', 'POST'])
def update(review_id):
    form = ReviewForm()
    review_to_update = Review.query.get(review_id)
    if form.validate_on_submit():
        review_to_update.task = review.task.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.task.data = todo_to_update.task
    return render_template('update.html', form=form)

@app.route('/delete/<int:review_id>')
def delete(review_id):
    review_to_delete = Review.query.get(review_id)
    db.session.delete(review_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

