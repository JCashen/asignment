from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from application.models import review, games

class ReviewCheck:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        all_reviews = review.query.all()
        for review in all_reviews:
            if review.review == field.data:
                raise ValidationError(self.message)

class ReviewForm(FlaskForm):
    review = StringField('Task',
            validators=[
                DataRequired(),
                ReviewCheck(message='That Review already exists')
            ]
         )

    submit = SubmitField('Add Todo')
    
