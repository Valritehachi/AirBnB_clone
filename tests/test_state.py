#!/usr/bin/python3
"""This code Defines unittests for the state model.

Unittest classes:
    TestState_save
    TestState_to_dict
"""


import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestStateInstantiation(unittest.TestCase):
    """Unit tests for testing the functionality of the State class."""

    def test_01_no_args_instantiates(self):
        """checks the functionality of the state class throughout the code."""
        state = State()
        self.assertEqual(State, type(state))

    def test_02_args_unused(self):
        """checks the functionality of the state class throughout the code."""
        state = State(None, 42, "unused")
        self.assertNotIn(None, state.__dict__.values())
        self.assertNotIn(42, state.__dict__.values())
        self.assertNotIn("unused", state.__dict__.values())

    def test_03_id_is_public_str(self):
        """checks the functionality of the state class throughout the code."""
        state = State()
        self.assertEqual(str, type(state.id))

    def test_04_created_at_is_public_datetime(self):
        """checks the functionality of the state class throughout the code."""
        state = State()
        self.assertEqual(datetime, type(state.created_at))

    def test_05_updated_at_is_public_datetime(self):
        """checks the functionality of the state class throughout the code."""
        state = State()
        self.assertEqual(datetime, type(state.updated_at))

    def test_06_name_is_public_str(self):
        """checks the functionality of the state class throughout the code."""
        state = State()
        self.assertEqual(str, type(state.name))

    def test_07_two_states_unique_ids(self):
        """checks the functionality of the state class throughout the code."""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_08_args_unused(self):
        """checks the functionality of the state class throughout the code."""
        st = State(None)
        self.assertNotIn(None, st.__dict__.values())

    def test_09_one_save(self):
        """checks the functionality of the state class throughout the code."""
        st = State()
        sleep(0.05)
        first_updated_at = st.updated_at
        st.save()
        self.assertLess(first_updated_at, st.updated_at)

    def test_10_two_saves(self):
        """checks the functionality of the state class throughout the code."""
        st = State()
        sleep(0.05)
        first_updated_at = st.updated_at
        st.save()
        second_updated_at = st.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        st.save()
        self.assertLess(second_updated_at, st.updated_at)

    def test_11_save_with_arg(self):
        """checks the functionality of the state class throughout the code."""
        st = State()
        with self.assertRaises(TypeError):
            st.save(None)

    def test_12_two_state_created_at(self):
        """checks the functionality of the state class throughout the code."""
        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.created_at, st2.created_at)

    def test_13_two_states__updated_at(self):
        """checks the functionality of the state class throughout the code."""
        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.updated_at, st2.updated_at)

    def test_14_to_dict_type(self):
        """checks the functionality of the state class throughout the code."""
        self.assertTrue(dict, type(State().to_dict()))

    def test_15_to_dict_contains_added_attributes(self):
        """checks the functionality of the state class throughout the code."""
        st = State()
        st.middle_name = "Holberton"
        st.my_number = 98
        self.assertEqual("Holberton", st.middle_name)
        self.assertIn("my_number", st.to_dict())

    def test_16_public_class_attribute(self):
        """checks the functionality of the state class throughout the code."""
        st = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(st))
        self.assertNotIn("name", st.__dict__)

    def test_17_updated_at_is_public_datetime(self):
        """checks the functionality of the state class throughout the code."""
        self.assertEqual(datetime, type(State().updated_at))

    def test_18_two_states_unique_ids(self):
        """checks the functionality of the state class throughout the code."""
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

    def test_19_to_dict_with_arg(self):
        """checks the functionality of the state class throughout the code."""
        st = State()
        with self.assertRaises(TypeError):
            st.to_dict(None)

    def test_20_no_args_instantiates(self):
        """checks the functionality of the state class throughout the code."""
        self.assertEqual(State, type(State()))

    def test_21_id_is_public_str(self):
        """checks the functionality of the state class throughout the code."""
        self.assertEqual(str, type(State().id))

    def test_22_created_at_is_public_datetime(self):
        """checks the functionality of the state class throughout the code."""
        self.assertEqual(datetime, type(State().created_at))


if __name__ == "__main__":
    unittest.main()
