import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models import storage
from pathlib import Path
import json
import re


class TestHBNBConsole(unittest.TestCase):
    def setUp(self):
        self.my_console = HBNBCommand()

    def test_emptyline(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("")

        result = mock_stdout.getvalue().strip()
        expected = ""
        self.assertEqual(result, expected)

    def test_console_all(self):
        all_keys = list(storage.all().keys())
        for key in all_keys:
            class_id = key.split(".")
            class_ = class_id[0]
            id_ = class_id[1]
            self.my_console.onecmd("destroy {} {}".format(class_, id_))

        new_model = BaseModel()
        storage.save()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("all")

        pattern = r'(\[[a-zA-Z]+\])'
        result = re.search(pattern, mock_stdout.getvalue()).group(1)
        expected = 11
        self.assertEqual(len(result), expected)

    def test_console_all_classname(self):
        all_keys = list(storage.all().keys())
        for key in all_keys:
            class_id = key.split(".")
            class_ = class_id[0]
            id_ = class_id[1]
            self.my_console.onecmd("destroy {} {}".format(class_, id_))

        new_model = BaseModel()
        storage.save()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("all BaseModel")

        pattern = r'(\[[a-zA-Z]+\])'
        result = re.search(pattern, mock_stdout.getvalue()).group(1)
        expected = 11
        self.assertEqual(len(result), expected)

    def test_console_destroy(self):
        new_model = BaseModel()
        new_model.save()
        new_model_id = new_model.id
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("destroy BaseModel {}".format(new_model_id))

        result = mock_stdout.getvalue().strip()
        expected = ""
        self.assertEqual(result, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("destroy")

        result = mock_stdout.getvalue().strip()
        expected = "** class name missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("destroy BaseModel")

        result = mock_stdout.getvalue().strip()
        expected = "** instance id missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("destroy Model {}".format(new_model_id))

        result = mock_stdout.getvalue().strip()
        expected = "** class doesn't exist **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("destroy BaseModel 123")

        result = mock_stdout.getvalue().strip()
        expected = "** no instance found **"
        self.assertEqual(result, expected)

    def test_console_create(self):
        all_keys = list(storage.all().keys())
        for key in all_keys:
            class_id = key.split(".")
            class_ = class_id[0]
            id_ = class_id[1]
            self.my_console.onecmd("destroy {} {}".format(class_, id_))
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("create BaseModel")

        result = mock_stdout.getvalue().strip()
        expected = list(storage.all().keys())[0].split(".")[1]
        self.assertEqual(result, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("create")

        result = mock_stdout.getvalue().strip()
        expected = "** class name missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("create Model")

        result = mock_stdout.getvalue().strip()
        expected = "** class doesn't exist **"
        self.assertEqual(result, expected)

    def test_console_show(self):
        model1 = BaseModel()
        model_id = model1.id
        storage.save()

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("show BaseModel {}".format(model_id))

        pattern = r'(\[[a-zA-Z]+\])'
        result = re.search(pattern, mock_stdout.getvalue()).group(1)
        expected = 11
        self.assertEqual(len(result), expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("show Model {}".format(model_id))

        result = mock_stdout.getvalue().strip()
        expected = "** class doesn't exist **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("show")

        result = mock_stdout.getvalue().strip()
        expected = "** class name missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_console.onecmd("show BaseModel 123")

        result = mock_stdout.getvalue().strip()
        expected = "** no instance found **"
        self.assertEqual(result, expected)
