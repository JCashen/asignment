from application import db



class games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String(30), nullable=False)


class review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(100), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
