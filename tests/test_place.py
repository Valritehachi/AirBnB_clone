#!/usr/bin/python3
"""This code should Define unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
"""


import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing of the Place class."""

    def test_01_no_args_instantiates(self):
        """functions to tests the functionality of the class model"""
        place = Place()
        self.assertEqual(Place, type(place))

    def test_02_args_unused(self):
        """functions to tests the functionality of the class model"""
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_03_id_is_public_str(self):
        """functions to tests the functionality of the class model"""
        place = Place()
        self.assertEqual(str, type(place.id))

    def test_04_created_at_is_public_datetime(self):
        """functions to tests the functionality of the class model"""
        place = Place()
        self.assertEqual(datetime, type(place.created_at))

    def test_05_updated_at_is_public_datetime(self):
        """functions to tests the functionality of the class model"""
        place = Place()
        self.assertEqual(datetime, type(place.updated_at))

    def test_06_city_id_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_07_user_id_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    def test_08_name_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    def test_09_description_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pl))
        self.assertNotIn("description", pl.__dict__)

    def test_10_number_rooms_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

    def test_11_number_bathrooms_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_12_max_guest_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_13_price_by_night_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

    def test_14_latitude_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pl))
        self.assertNotIn("latitude", pl.__dict__)

    def test_15_longitude_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pl))
        self.assertNotIn("longitude", pl.__dict__)

    def test_16_amenity_ids_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)

    def test_17_two_places_unique_ids(self):
        """functions to tests the functionality of the class model"""
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_18_two_places_different_created_at(self):
        """functions to tests the functionality of the class model"""
        pl1 = Place()
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_19_two_places_different_updated_at(self):
        """functions to tests the functionality of the class model"""
        pl1 = Place()
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def test_20_two_saves(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        first_updated_at = pl.updated_at
        pl.save()
        second_updated_at = pl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        pl.save()
        self.assertLess(second_updated_at, pl.updated_at)

    def test_21_save_with_arg(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        with self.assertRaises(TypeError):
            pl.save(None)

    def test_22_to_dict_type(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertTrue(dict, type(pl.to_dict()))

    def test_23_to_dict_contains_added_attributes(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        pl.middle_name = "Holberton"
        pl.my_number = 98
        self.assertEqual("Holberton", pl.middle_name)
        self.assertIn("my_number", pl.to_dict())

    def test_24_no_args_instantiates(self):
        """functions to tests the functionality of the class model"""
        self.assertEqual(Place, type(Place()))

    def test_25_args_unused(self):
        """functions to tests the functionality of the class model"""
        self.assertNotIn(None, Place().__dict__.values())

    def test_26_id_is_public_str(self):
        """functions to tests the functionality of the class model"""
        self.assertEqual(str, type(Place().id))

    def test_27_created_at_is_public_datetime(self):
        """functions to tests the functionality of the class model"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_28_updated_at_is_public_datetime(self):
        """functions to tests the functionality of the class model"""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_29_city_id_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_30_user_id_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    def test_31_name_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    def test_32_description_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pl))
        self.assertNotIn("desctiption", pl.__dict__)

    def test_33_number_rooms_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

    def test_34_number_bathrooms_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_35_max_guest_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_36_price_by_night_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

    def test_37_latitude_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pl))
        self.assertNotIn("latitude", pl.__dict__)

    def test_38_longitude_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pl))
        self.assertNotIn("longitude", pl.__dict__)

    def test_37_amenity_ids_is_public_class_attribute(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)

    def test_38_two_places_unique_ids(self):
        """functions to tests the functionality of the class model"""
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_39_two_places_different_created_at(self):
        """functions to tests the functionality of the class model"""
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_40_two_places_different_updated_at(self):
        """functions to tests the functionality of the class model"""
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def test_41_args_unused(self):
        """functions to tests the functionality of the class model"""
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())

    def test_42_one_save(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        first_updated_at = pl.updated_at
        pl.save()
        self.assertLess(first_updated_at, pl.updated_at)

    def test_43_two_saves(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        first_updated_at = pl.updated_at
        pl.save()
        second_updated_at = pl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        pl.save()
        self.assertLess(second_updated_at, pl.updated_at)

    def test_44_save_with_arg(self):
        """functions to tests the functionality of the class model"""
        pl = Place()
        with self.assertRaises(TypeError):
            pl.save(None)


if __name__ == "__main__":
    unittest.main()
