from application import db
from application.models import Games 


db.drop_all()
db.create_all()

new_game = Games(game = "CSGO: ")
db.session.add(new_game)
new_game = Games(game = "OSU: ")
db.session.add(new_game)
new_game = Games(game = "Fallout 76: ")
db.session.add(new_game)
new_game = Games(game = "NieR:Automata: ")
db.session.add(new_game)
new_game = Games(game = "GTA V: ")
db.session.add(new_game)
new_game = Games(game = "DOOM: ")
db.session.add(new_game)
new_game = Games(game = "GTFO: ")
db.session.add(new_game)
new_game = Games(game = "Raft: ")
db.session.add(new_game)
db.session.commit()
