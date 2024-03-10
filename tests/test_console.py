#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    create, show, all, etc.
"""

import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the whole console"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout, command):
        """Unit tests for the whole console"""
        with patch('builtins.input', return_value=command):
            self.console.cmdloop()
            self.assertEqual(
                mock_stdout.getvalue().strip(),
                expected_output.strip()
            )

    def test_02_prompt_string(self):
        """Unit tests for the whole console"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_03_empty_line(self):
        """Unit tests for the whole console"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_04_help(self):
        """Unit tests for the whole console"""
        h = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h, output.getvalue().strip())

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_08_create_missing_class(self):
        """Unit tests for the whole console"""
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_09_create_invalid_class(self):
        """Unit tests for the whole console"""
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_10_create_invalid_syntax(self):
        """Unit tests for the whole console"""
        correct = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())
        correct = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_11_show_invalid_class(self):
        """Unit tests for the whole console"""
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show InvalidClass 1234"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_12_show_invalid_id(self):
        """Unit tests for the whole console"""
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel invalid_id"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_13_destroy_invalid_class(self):
        """Unit tests for the whole console"""
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy InvalidClass 1234"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_14_destroy_invalid_id(self):
        """Unit tests for the whole console"""
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(
                HBNBCommand().onecmd("destroy BaseModel invalid_id")
            )
            self.assertEqual(correct, output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
