#!/usr/bin/python3
"""This code defines unittests for the city model.

Unittest classes:
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """Unit tests for the City class."""

    def test_01_no_args_instantiates(self):
        """functions for city model to show its functionality."""
        city = City()
        self.assertEqual(City, type(city))

    def test_02_args_unused(self):
        """functions for Tests for city model to show its functionality."""
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_03_args_unused(self):
        """functions for Tests for city model to show its functionality."""
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_04_id_is_public_str(self):
        """functions for Tests for city model to show its functionality."""
        city = City()
        self.assertEqual(str, type(city.id))

    def test_05_created_at_is_public_datetime(self):
        """functions for Tests for city model to show its functionality."""
        city = City()
        self.assertEqual(datetime, type(city.created_at))

    def test_06_updated_at_is_public_datetime(self):
        """functions for Tests for city model to show its functionality."""
        city = City()
        self.assertEqual(datetime, type(city.updated_at))

    def test_07_name_is_public_class_attribute(self):
        """functions for Tests for city model to show its functionality."""
        city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(City()))
        self.assertNotIn("name", city.__dict__)

    def test_08_state_id_is_public_class_attribute(self):
        """functions for Tests for city model to show its functionality."""
        city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(City()))
        self.assertNotIn("state_id", city.__dict__)

    def test_09_two_cities_unique_ids(self):
        """functions for Tests for city model to show its functionality."""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_10_two_cities_different_created_at(self):
        """functions for Tests for city model to show its functionality."""
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_11_two_cities_different_updated_at(self):
        """functions for Tests for city model to show its functionality."""
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_12_to_dict_type(self):
        """functions for Tests for city model to show its functionality."""
        city = City()
        self.assertTrue(dict, type(city.to_dict()))

    def test_13_id_is_public_str(self):
        """functions for Tests for city model to show its functionality."""
        city = City()
        self.assertEqual(str, type(city.id))

    def test_14_created_at_is_public_datetime(self):
        """functions for Tests for city model to show its functionality."""
        city = City()
        self.assertEqual(datetime, type(city.created_at))

    def test_15_updated_at_is_public_datetime(self):
        """functions for Tests for city model to show its functionality."""
        city = City()
        self.assertEqual(datetime, type(city.updated_at))

    def test_16_state_id_is_public_class_attribute(self):
        """functions for Tests for city model to show its functionality."""
        city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(city))
        self.assertNotIn("state_id", city.__dict__)

    def test_17_name_is_public_class_attribute(self):
        """functions for Tests for city model to show its functionality."""
        city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

    def test_18_two_cities_unique_ids(self):
        """functions for Tests for city model to show its functionality."""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_19_two_cities_different_created_at(self):
        """functions for Tests for city model to show its functionality."""
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_20_two_cities_different_updated_at(self):
        """functions for Tests for city model to show its functionality."""
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)


if __name__ == "__main__":
    unittest.main()
