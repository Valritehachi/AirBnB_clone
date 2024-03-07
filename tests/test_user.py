#!/usr/bin/python3
"""This code Defines unittests for the user model.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""


import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """a class showing all the tests for the user model"""
    def test_01_no_args_instantiates(self):
        """unit test creating User instance without affecting instance"""
        user = User()
        self.assertEqual(User, type(user))

    def test_02_args_unused(self):
        """unit test creating User instance without affecting instance"""
        us = User(None)
        self.assertNotIn(None, us.__dict__.values())

    def test_03_id_is_public_str(self):
        """unit test creating User instance without affecting instance"""
        user = User()
        self.assertEqual(str, type(user.id))

    def test_04_created_at_is_public_datetime(self):
        """unit test creating User instance without affecting instance"""
        user = User()
        self.assertEqual(datetime, type(user.created_at))

    def test_05_updated_at_is_public_datetime(self):
        """unit test creating User instance without affecting instance"""
        user = User()
        self.assertEqual(datetime, type(user.updated_at))

    def test_06_email_attribute(self):
        """unit test creating User instance without affecting instance"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertEqual("", user.email)

    def test_07_password_attribute(self):
        """unit test creating User instance without affecting instance"""
        user = User()
        self.assertTrue(hasattr(user, 'password'))
        self.assertEqual("", user.password)

    def test_08_first_name_attribute(self):
        """unit test creating User instance without affecting instance"""
        user = User()
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertEqual("", user.first_name)

    def test_09_last_name_attribute(self):
        """unit test creating User instance without affecting instance"""
        user = User()
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual("", user.last_name)

    def test_10_to_dict_type(self):
        """unit test creating User instance without affecting instance"""
        user = User()
        self.assertTrue(dict, type(user.to_dict()))

    def test_11_two_users_different_updated_at(self):
        """unit test creating User instance without affecting instance"""
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_12_to_dict_contains_attributes(self):
        """unit test creating User instance without affecting instance"""
        user = User()
        user.email = "test@example.com"
        user.password = "secure_password"
        user.first_name = "John"
        user.last_name = "Doe"
        user_dict = user.to_dict()
        self.assertEqual("test@example.com", user_dict['email'])
        self.assertEqual("secure_password", user_dict['password'])
        self.assertEqual("John", user_dict['first_name'])
        self.assertEqual("Doe", user_dict['last_name'])

    def test_13_no_args_instantiates(self):
        """unit test creating User instance without affecting instance"""
        self.assertEqual(User, type(User()))

    def test_14_two_users_different_created_at(self):
        """unit test creating User instance without affecting instance"""
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_15_id_is_public_str(self):
        """unit test creating User instance without affecting instance"""
        self.assertEqual(str, type(User().id))

    def test_16_created_at_is_public_datetime(self):
        """unit test creating User instance without affecting instance"""
        self.assertEqual(datetime, type(User().created_at))

    def test_17_updated_at_is_public_datetime(self):
        """unit test creating User instance without affecting instance"""
        self.assertEqual(datetime, type(User().updated_at))

    def test_18_email_is_public_str(self):
        """unit test creating User instance without affecting instance"""
        self.assertEqual(str, type(User.email))

    def test_19_password_is_public_str(self):
        """unit test creating User instance without affecting instance"""
        self.assertEqual(str, type(User.password))

    def test_20_first_name_is_public_str(self):
        """unit test creating User instance without affecting instance"""
        self.assertEqual(str, type(User.first_name))

    def test_21_last_name_is_public_str(self):
        """unit test creating User instance without affecting instance"""
        self.assertEqual(str, type(User.last_name))

    def test_22_two_users_unique_ids(self):
        """unit test creating User instance without affecting instance"""
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)


if __name__ == "__main__":
    unittest.main()
