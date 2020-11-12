from application import db

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review  = db.Column(db.String(30), nullable=False)
    
