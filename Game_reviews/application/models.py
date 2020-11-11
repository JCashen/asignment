from application import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gameid = db.Column(db.Integer, db.ForeignKey('game.id'))
    review = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Boolean, default=False)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String(30), nullable=False)
