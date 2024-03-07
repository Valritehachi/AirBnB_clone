#!/usr/bin/python3
"""This test defines unittests for models/review.py.

Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""


import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    """unit tests for the review modal"""
    def test_01_no_args_instantiates(self):
        """functions Tests for city model to show its functionality."""
        review = Review()
        self.assertEqual(Review, type(review))

    def test_02_args_unused(self):
        """functions Tests for city model to show its functionality."""
        self.assertNotIn(None, Review().__dict__.values())

    def test_03_id_is_public_str(self):
        """functions Tests for city model to show its functionality."""
        self.assertEqual(str, type(Review().id))

    def test_04_created_at_is_public_datetime(self):
        """functions Tests for city model to show its functionality."""
        self.assertEqual(datetime, type(Review().created_at))

    def test_05_updated_at_is_public_datetime(self):
        """functions Tests for city model to show its functionality."""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_06_place_id_is_public_class_attribute(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_07_user_id_is_public_class_attribute(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_08_text_is_public_class_attribute(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_09_two_reviews_unique_ids(self):
        """functions Tests for city model to show its functionality."""
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_10_two_reviews_different_created_at(self):
        """functions Tests for city model to show its functionality."""
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_11_two_reviews_different_updated_at(self):
        """functions Tests for city model to show its functionality."""
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_12_args_unused(self):
        """functions Tests for city model to show its functionality."""
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_13_one_save(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        first_updated_at = rv.updated_at
        rv.save()
        self.assertLess(first_updated_at, rv.updated_at)

    def test_14_two_saves(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        first_updated_at = rv.updated_at
        rv.save()
        second_updated_at = rv.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        rv.save()
        self.assertLess(second_updated_at, rv.updated_at)

    def test_15_save_with_arg(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        with self.assertRaises(TypeError):
            rv.save(None)

    def test_16_to_dict_type(self):
        """functions Tests for city model to show its functionality."""
        self.assertTrue(dict, type(Review().to_dict()))

    def test_17_to_dict_contains_added_attributes(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        rv.middle_name = "Holberton"
        rv.my_number = 98
        self.assertEqual("Holberton", rv.middle_name)
        self.assertIn("my_number", rv.to_dict())

    def test_18_to_dict_with_arg(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        with self.assertRaises(TypeError):
            rv.to_dict(None)

    def test_19_no_args_instantiates(self):
        """functions Tests for city model to show its functionality."""
        self.assertEqual(Review, type(Review()))

    def test_20_id_is_public_str(self):
        """functions Tests for city model to show its functionality."""
        self.assertEqual(str, type(Review().id))

    def test_21_created_at_is_public_datetime(self):
        """functions Tests for city model to show its functionality."""
        self.assertEqual(datetime, type(Review().created_at))

    def test_22_updated_at_is_public_datetime(self):
        """functions Tests for city model to show its functionality."""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_23_place_id_is_public_class_attribute(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_24_user_id_is_public_class_attribute(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_25_text_is_public_class_attribute(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_26_two_reviews_unique_ids(self):
        """functions Tests for city model to show its functionality."""
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_27_two_reviews_different_created_at(self):
        """functions Tests for city model to show its functionality."""
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_28_two_reviews_different_updated_at(self):
        """functions Tests for city model to show its functionality."""
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_29_args_unused(self):
        """functions Tests for city model to show its functionality."""
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_30_one_save(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        self.assertLess(first_updated_at, rv.updated_at)

    def test_31_two_saves(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        second_updated_at = rv.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rv.save()
        self.assertLess(second_updated_at, rv.updated_at)

    def test_32_save_with_arg(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        with self.assertRaises(TypeError):
            rv.save(None)

    def test_33_to_dict_type(self):
        """functions Tests for city model to show its functionality."""
        self.assertTrue(dict, type(Review().to_dict()))

    def test_34_to_dict_contains_added_attributes(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        rv.middle_name = "Holberton"
        rv.my_number = 98
        self.assertEqual("Holberton", rv.middle_name)
        self.assertIn("my_number", rv.to_dict())

    def test_35_to_dict_with_arg(self):
        """functions Tests for city model to show its functionality."""
        rv = Review()
        with self.assertRaises(TypeError):
            rv.to_dict(None)


if __name__ == "__main__":
    unittest.main()
