import random
import unittest
import os

from app.models.user import User

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.user_obj = User()
        self.user = {}

    def tearDown(self):
        self.user_obj.destroy()
    
    def test_create_user(self):
        user_info = {
            "email": "ludim@gmail.com",
            "password": "ludim2020",
            "role_id": 2
        }

        user = self.user_obj.get(user_info["email"])

        if not user:
            user = self.user_obj.create(user_info)
        self.assertIsNotNone(user)

    def test_select_users(self):
        self.user_obj = User()
        users = self.user_obj.all()
        self.assertIsNotNone(users)

    def test_remove_existent_user(self):
        email = "ludim@gmail.com"
        self.user_obj = User()
        user = self.user_obj.get(email)
        if user:
            user = self.user_obj.delete(email)
            self.assertTrue(user)
        else:
            self.assertFalse(user)

    def test_edit_user_password(self):
        self.user_obj = User()
        user_info = {
            "email": "ludim.anel@gmail.com",
            "password": "ludimanel"
        }
        user = self.user_obj.edit(user_info)
        self.assertIsNotNone(user)
        self.assertEqual(user, {'id': 38, 'email': 'ludim.anel@gmail.com', 'password': '', 'role_id': 2})
        self.user['password'] = user["password"]

    def test_edit_user_role(self):
        self.user_obj = User()
        user_info = {
            "email": "ludim.anel@gmail.com",
            "role_id": 1
        }
        user = self.user_obj.edit(user_info)
        self.assertEqual(user, {'id': 38, 'email': 'ludim.anel@gmail.com', 'password': '', 'role_id': 1})

    def test_edit_user_role_password(self):
        self.user_obj = User()
        user_info = {
            "email": "ludim.anel@gmail.com",
            "password": "ludim2020",
            "role_id": 2
        }
        user = self.user_obj.edit(user_info)
        self.assertEqual(user, {'id': 38, 'email': 'ludim.anel@gmail.com', 'password': '', 'role_id': 2})
