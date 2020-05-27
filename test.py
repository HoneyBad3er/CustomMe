
import re
import unittest
from flask import current_app

from app import create_app, db
from app.db_models import UserData, DevicesData


class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_home_page(self):
        response = self.client.get('/main')
        self.assertEqual(response.status_code, 200)

    def test_set_eq_page(self):
        response = self.client.get('/set_eq')
        self.assertEqual(response.status_code, 302)

    def test_get_eq_page(self):
        response = self.client.post('/get_eq', data={
            'headphones_name': 'void',
            'player_name': 'void',
            'genre': 'rock'
        })
        self.assertEqual(response.status_code, 302)

    def test_register_and_login(self):
        # register a new account
        response = self.client.post('/signup', data={
            'username': 'john',
            'email': 'john@example.com',
            'password': 'cat',
            'password2': 'cat'
        })
        self.assertEqual(response.status_code, 200)

        # login with the new account
        response = self.client.post('/login', data={
            'email': 'john@example.com',
            'password': 'cat'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # log out
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
