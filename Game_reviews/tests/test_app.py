import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Review, Games

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
        SECRET_KEY='TEST_SECRET_KEY',
        DEBUG=True)
        return app

    def setUp(self):
        db.create_all()
        review = Review(review='The Best Game Ever', game_id='1')
        game1 = Games(game='NieR:Automata' )
        db.session.add(review)
        db.session.add(game1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def text_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code,200)

    def test_add_get(self):
        response = self.client.get(url_for('add'))  
        self.assertEqual(response.status_code,200)

    def test_add1_get(self):
        response = self.client.get(url_for('add1', idnum=1))  
        self.assertEqual(response.status_code,200)   

    def test_updateloc_get(self):
        response = self.client.get(url_for("updateloc", idnum=1))
        self.assertEqual(response.status_code,200)

    def test_updateact_get(self):
        response = self.client.get(url_for("updateact", idnum=1))
        self.assertEqual(response.status_code,200)

    def test_viewactivity_get(self):
        response = self.client.get(url_for("viewactivity", idnum=1))
        self.assertEqual(response.status_code,200)

    def test_deleteloc_get(self):
        response = self.client.get(url_for("deleteloc", idnum=1))
        self.assertEqual(response.status_code,302)

    def test_deleteact_get(self):
        response = self.client.get(url_for("deleteact", idnum=1))
        self.assertEqual(response.status_code,302)    
