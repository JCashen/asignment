from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from application.models import Review, Games

class ReviewCheck:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        all_reviews = Reviews.query.all()
        for todo in all_reviews:
            if todo.task == field.data:
                raise ValidationError(self.message)

class ReviewForm(FlaskForm):
    task = StringField('Task',
            validators=[
                DataRequired(),
                ReviewCheck(message='That Review  already exists')
            ]
         )

    submit = SubmitField('Add Todo')
    
