from unittest import TestCase
from app import app
from flask import session, request
from boggle import Boggle

boggle_game = Boggle()

class FlaskTests(TestCase):
    @classmethod
    def setUpClass(cls):
        with app.test_client() as client: 
            res = client.get('/')
            session['game'] = boggle_game.make_board()

    def test_get_index(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Boogle Game</h1>', html)

    def test_check_word(self):
        with app.test_client() as client: 
            with client.session_transaction() as change_session:
                change_session['game'] = boggle_game.make_board()
        
            res = client.get('/guess-word?guess=word')

            self.assertEqual(res.status_code, 200)
            self.assertEqual(request.args['guess'], 'word')


    # def test_get_top_score(self):
    #     with app.test_client() as client:
    #         with client.session_transaction() as change_session:
    #             change_session['times-played'] = 1
    #             change_session['top-score'] = 0
    #         res = client.post('/top-score', data={'score': 1})


    #         self.assertEqual(res.status_code, 200)
