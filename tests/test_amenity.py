#!/usr/bin/python3
"""This code defines unittests for the amenity modal.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""


import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenityInstantiation(unittest.TestCase):
    """Unit tests for testing the functionality of the Amenity class."""

    def test_01_no_args_instantiates(self):
        """functions to test effectiveness of the amenity class model."""
        self.assertEqual(Amenity, type(Amenity()))

    def test_02_args_unused(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity(None, 42, "unused")
        self.assertNotIn(None, amenity.__dict__.values())
        self.assertNotIn(42, amenity.__dict__.values())
        self.assertNotIn("unused", amenity.__dict__.values())

    def test_03_id_is_public_str(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity()
        self.assertEqual(str, type(amenity.id))

    def test_04_created_at_is_public_datetime(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity()
        self.assertEqual(datetime, type(amenity.created_at))

    def test_05_updated_at_is_public_datetime(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity()
        self.assertEqual(datetime, type(amenity.updated_at))

    def test_06_name_is_public_str(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity()
        self.assertEqual(str, type(amenity.name))

    def test_07_two_amenities_unique_ids(self):
        """functions to test effectiveness of the amenity class model."""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_08_no_args_instantiates(self):
        """functions to test effectiveness of the amenity class model."""
        self.assertEqual(Amenity, type(Amenity()))

    def test_09_args_unused(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity(None, 42, "unused")
        self.assertNotIn(None, amenity.__dict__.values())
        self.assertNotIn(42, amenity.__dict__.values())
        self.assertNotIn("unused", amenity.__dict__.values())

    def test_10_id_is_public_str(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity()
        self.assertEqual(str, type(amenity.id))

    def test_11_created_at_is_public_datetime(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity()
        self.assertEqual(datetime, type(amenity.created_at))

    def test_12_updated_at_is_public_datetime(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity()
        self.assertEqual(datetime, type(amenity.updated_at))

    def test_13_name_is_public_str(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity()
        self.assertEqual(str, type(amenity.name))

    def test_14_two_amenities_unique_ids(self):
        """functions to test effectiveness of the amenity class model."""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_15_two_amenities_different_created_at(self):
        """functions to test effectiveness of the amenity class model."""
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_16_two_amenities_different_updated_at(self):
        """functions to test effectiveness of the amenity class model."""
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_17_args_unused(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_18_one_save(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity()
        sleep(0.05)
        first_updated_at = amenity.updated_at
        amenity.save()
        self.assertLess(first_updated_at, amenity.updated_at)

    def test_19_two_saves(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity()
        sleep(0.05)
        first_updated_at = amenity.updated_at
        amenity.save()
        second_updated_at = amenity.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amenity.save()
        self.assertLess(second_updated_at, amenity.updated_at)

    def test_20_save_with_arg(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save(None)

    def test_21_save_updates_file(self):
        """functions to test effectiveness of the amenity class model."""
        amenity = Amenity()
        amenity.save


if __name__ == "__main__":
    unittest.main()
