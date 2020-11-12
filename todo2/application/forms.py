from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from application.models import Todos

class ReviewsCheck:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        all_reviews = Reviews.query.all()
        for reviews in all_reviews:
            if reviews.review == field.data:
                raise ValidationError(self.message)

class ReviewsForm(FlaskForm):
    review = StringField('Review',
            validators=[
                DataRequired(),
                TodoCheck(message='That Review already exists')
            ]
         )

    submit = SubmitField('Add Review')
    
