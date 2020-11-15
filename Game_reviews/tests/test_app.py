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

    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_add_get(self):
        response = self.client.get(url_for('add', review_id=1))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update', review_id=1))
        self.assertEqual(response.status_code,200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', review_id=1))
        self.assertEqual(response.status_code,302)




