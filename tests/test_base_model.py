#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_01_init_without_args(self):
        """unittests for base model file testcase."""
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_02_no_args_instantiates(self):
        """unittests for base model file testcase."""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_03_id_is_public_str(self):
        """unittests for base model file testcase."""
        self.assertEqual(str, type(BaseModel().id))

    def test_04_created_at_is_public_datetime(self):
        """unittests for base model file testcase."""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_05_updated_at_is_public_datetime(self):
        """unittests for base model file testcase."""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_06_two_models_unique_ids(self):
        """unittests for base model file testcase."""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_07_two_models_different_created_at(self):
        """unittests for base model file testcase."""
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_08_to_dict_type(self):
        """unittests for base model file testcase."""
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_09_to_dict_with_arg(self):
        """unittests for base model file testcase."""
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

    def test_10_save(self):
        """unittests for base model file testcase."""
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_11_saves(self):
        """unittests for base model file testcase."""
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_12_save_with_arg(self):
        """unittests for base model file testcase."""
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)


if __name__ == '__main__':
    unittest.main()
