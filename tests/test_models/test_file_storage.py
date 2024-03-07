import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import json


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.base1 = BaseModel()

    def test_file_storage_all_method(self):
        dict_ = storage.all()
        self.assertTrue(type(dict_), dict)
        self.assertGreater(len(dict_.keys()), 0)

    def test_file_storage_save(self):
        storage.save()

        nb_chars = 0
        with open("file.json", "r", encoding="utf-8") as file:
            content = json.load(file)
            nb_chars = len(content)
        self.assertGreater(nb_chars, 0)

    def test_file_storage_new(self):
        storage.new(self.base1)

        nb_chars = 0
        with open("file.json", "r", encoding="utf-8") as file:
            content = json.load(file)
            nb_chars = len(content)
        self.assertGreater(nb_chars, 0)

    def test_file_storage_reload(self):
        storage.reload()
        dict_ = storage.all()
        self.assertTrue(type(dict_), dict)
        self.assertGreater(len(dict_.keys()), 0)
