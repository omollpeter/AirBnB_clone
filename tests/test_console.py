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
    def test_emptyline(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("")

        result = f.getvalue().strip()
        expected = ""
        self.assertEqual(result, expected)

    def test_console_all(self):
        all_keys = list(storage.all().keys())
        for key in all_keys:
            class_id = key.split(".")
            class_ = class_id[0]
            id_ = class_id[1]
            HBNBCommand().onecmd("destroy {} {}".format(class_, id_))

        new_model = BaseModel()
        storage.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all")

        pattern = r'(\[[a-zA-Z]+\])'
        result = re.search(pattern, f.getvalue()).group(1)
        expected = 11
        self.assertEqual(len(result), expected)

    def test_console_all_classname(self):
        all_keys = list(storage.all().keys())
        for key in all_keys:
            class_id = key.split(".")
            class_ = class_id[0]
            id_ = class_id[1]
            HBNBCommand().onecmd("destroy {} {}".format(class_, id_))

        new_model = BaseModel()
        storage.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")

        pattern = r'(\[[a-zA-Z]+\])'
        result = re.search(pattern, f.getvalue()).group(1)
        expected = 11
        self.assertEqual(len(result), expected)

    def test_console_class_name_all(self):
        all_keys = list(storage.all().keys())
        for key in all_keys:
            class_id = key.split(".")
            class_ = class_id[0]
            id_ = class_id[1]
            HBNBCommand().onecmd("destroy {} {}".format(class_, id_))

        new_model = BaseModel()
        storage.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")

        result = f.getvalue().strip()
        self.assertGreater(len(result), 0)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Model.all()")

        result = f.getvalue().strip()
        expected = "** class doesn't exist **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Model.all")

        result = f.getvalue().strip()
        expected = "** unknown command **"
        self.assertEqual(result, expected)

    def test_console_help_all(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help all")

        result = f.getvalue().strip()
        expected = """\
Prints a list of all string representation of all \
instances based or not on the class name.\n\
Ex: $ all BaseModel or $ all"""
        self.assertEqual(result, expected)

    def test_console_destroy(self):
        new_model = BaseModel()
        new_model.save()
        new_model_id = new_model.id
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel {}".format(new_model_id))

        result = f.getvalue().strip()
        expected = ""
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")

        result = f.getvalue().strip()
        expected = "** class name missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")

        result = f.getvalue().strip()
        expected = "** instance id missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Model {}".format(new_model_id))

        result = f.getvalue().strip()
        expected = "** class doesn't exist **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 123")

        result = f.getvalue().strip()
        expected = "** no instance found **"
        self.assertEqual(result, expected)

    def test_console_class_name_destroy(self):
        new_model = BaseModel()
        new_model.save()
        new_model_id = new_model.id
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy({})".format(new_model_id))

        result = f.getvalue().strip()
        expected = ""
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy")

        result = f.getvalue().strip()
        expected = "** unknown command **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")

        result = f.getvalue().strip()
        expected = "** instance id missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Model.destroy({})".format(new_model_id))

        result = f.getvalue().strip()
        expected = "** class doesn't exist **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy(123)")

        result = f.getvalue().strip()
        expected = "** no instance found **"
        self.assertEqual(result, expected)

    def test_console_help_destroy(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")

        result = f.getvalue().strip()
        expected = """\
Deletes an instance based on the class name and id \
(save the change into the JSON file).\n\
Ex: $ destroy BaseModel 1234-1234-1234\
"""
        self.assertEqual(result, expected)

    def test_console_create(self):
        all_keys = list(storage.all().keys())
        for key in all_keys:
            class_id = key.split(".")
            class_ = class_id[0]
            id_ = class_id[1]
            HBNBCommand().onecmd("destroy {} {}".format(class_, id_))
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        result = f.getvalue().strip()
        expected = list(storage.all().keys())[0].split(".")[1]
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")

        result = f.getvalue().strip()
        expected = "** class name missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Model")

        result = f.getvalue().strip()
        expected = "** class doesn't exist **"
        self.assertEqual(result, expected)

    def test_console_help_create(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help create")

        result = f.getvalue().strip()
        expected = """\
Creates a new instance of BaseModel, saves it \
(to the JSON file) and prints the id.\n\
Example: create BaseModel\
"""
        self.assertEqual(result, expected)

    def test_console_show(self):
        model1 = BaseModel()
        model_id = model1.id
        storage.save()

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(model_id))

        pattern = r'(\[[a-zA-Z]+\])'
        result = re.search(pattern, f.getvalue()).group(1)
        expected = 11
        self.assertEqual(len(result), expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show Model {}".format(model_id))

        result = f.getvalue().strip()
        expected = "** class doesn't exist **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show")

        result = f.getvalue().strip()
        expected = "** class name missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")

        result = f.getvalue().strip()
        expected = "** instance id missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 123")

        result = f.getvalue().strip()
        expected = "** no instance found **"
        self.assertEqual(result, expected)

    def test_console_class_name_show(self):
        model1 = BaseModel()
        model_id = model1.id
        storage.save()

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show({})".format(model_id))

        pattern = r'(\[[a-zA-Z]+\])'
        result = re.search(pattern, f.getvalue()).group(1)
        expected = 11
        self.assertEqual(len(result), expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Model.show({})".format(model_id))

        result = f.getvalue().strip()
        expected = "** class doesn't exist **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show")

        result = f.getvalue().strip()
        expected = "** unknown command **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")

        result = f.getvalue().strip()
        expected = "** instance id missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(123)")

        result = f.getvalue().strip()
        expected = "** no instance found **"
        self.assertEqual(result, expected)

    def test_console_help_show(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help show")

        result = f.getvalue().strip()
        expected = """\
Prints the string representation of an \
instance based on the class name and id.\n\
Ex: $ show BaseModel 1234-1234-1234\
"""
        self.assertEqual(result, expected)

    def test_console_count(self):
        all_keys = list(storage.all().keys())
        for key in all_keys:
            class_id = key.split(".")
            class_ = class_id[0]
            id_ = class_id[1]
            HBNBCommand().onecmd("destroy {} {}".format(class_, id_))

        model1 = BaseModel()
        model_id = model1.id
        storage.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")

        result = f.getvalue().strip()
        expected = "1"
        self.assertEqual(result, expected)

        HBNBCommand().onecmd("destroy BaseModel {}".format(model_id))
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")

        result = f.getvalue().strip()
        expected = "0"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("count Model")

        result = f.getvalue().strip()
        expected = "** class doesn't exist **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("count")

        result = f.getvalue().strip()
        expected = "** class name missing **"
        self.assertEqual(result, expected)

    def test_console_class_name_count(self):
        all_keys = list(storage.all().keys())
        for key in all_keys:
            class_id = key.split(".")
            class_ = class_id[0]
            id_ = class_id[1]
            HBNBCommand().onecmd("destroy {} {}".format(class_, id_))

        model1 = BaseModel()
        model_id = model1.id
        storage.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")

        result = f.getvalue().strip()
        expected = "1"
        self.assertEqual(result, expected)

        HBNBCommand().onecmd("destroy BaseModel {}".format(model_id))
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")

        result = f.getvalue().strip()
        expected = "0"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Model.count()")

        result = f.getvalue().strip()
        expected = "** class doesn't exist **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Basemodel.count")

        result = f.getvalue().strip()
        expected = "** unknown command **"
        self.assertEqual(result, expected)

    def test_console_help_count(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help count")

        result = f.getvalue().strip()
        expected = """\
Prints count of instances based on class name\n\
Ex: $ count BaseModel\
"""
        self.assertEqual(result, expected)

    def test_console_quit(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("quit")

        result = f.getvalue().strip()
        expected = ""
        self.assertEqual(result, expected)

    def test_console_EOF(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")

        result = f.getvalue().strip()
        expected = ""
        self.assertEqual(result, expected)

    def test_console_update(self):
        model1 = BaseModel()
        model_id = model1.id
        storage.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {} type base".format(
                model_id
            ))

        result = f.getvalue().strip()
        expected = ""
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update Model {} type name".format(model_id))

        result = f.getvalue().strip()
        expected = "** class doesn't exist **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update")

        result = f.getvalue().strip()
        expected = "** class name missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")

        result = f.getvalue().strip()
        expected = "** instance id missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 123 type name")

        result = f.getvalue().strip()
        expected = "** no instance found **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {}".format(model_id))

        result = f.getvalue().strip()
        expected = "** attribute name missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {} type".format(model_id))

        result = f.getvalue().strip()
        expected = "** value missing **"
        self.assertEqual(result, expected)

    def test_console_class_name_update(self):
        model1 = BaseModel()
        model_id = model1.id
        storage.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update({}, type, base)".format(
                model_id
            ))

        result = f.getvalue().strip()
        expected = ""
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Model.update({}, age, 89)".format(model_id))

        result = f.getvalue().strip()
        expected = "** class doesn't exist **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Basemodel.update")

        result = f.getvalue().strip()
        expected = "** unknown command **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")

        result = f.getvalue().strip()
        expected = "** instance id missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(123, type, name)")

        result = f.getvalue().strip()
        expected = "** no instance found **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update({})".format(model_id))

        result = f.getvalue().strip()
        expected = "** attribute name missing **"
        self.assertEqual(result, expected)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update({}, type)".format(model_id))

        result = f.getvalue().strip()
        expected = "** value missing **"
        self.assertEqual(result, expected)

    def test_console_class_name_update_with_dict(self):
        model1 = BaseModel()
        model_id = model1.id
        storage.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update({}, {})".format(
                model_id,
                {"age": 89}
            ))

        result = f.getvalue().strip()
        expected = ""
        self.assertEqual(result, expected)

    def test_console_help_update(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help update")

        result = f.getvalue().strip()
        expected = """\
Updates an instance based on the class name \
and id by adding or updating attribute (save the \
change into the JSON file).\n\
Ex: $ update BaseModel 1234-1234-1234 email 'bnb@mail.com'\
"""
        self.assertEqual(result, expected)

    def test_console_BaseModel_all(self):
        all_keys = list(storage.all().keys())
        for key in all_keys:
            class_id = key.split(".")
            class_ = class_id[0]
            id_ = class_id[1]
            HBNBCommand().onecmd("destroy {} {}".format(class_, id_))

        new_model = BaseModel()
        storage.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")

        result = f.getvalue().strip()
        self.assertGreater(len(result), 0)
