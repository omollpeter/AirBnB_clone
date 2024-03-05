import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base1 = BaseModel()

    def test_base_model_instance_id(self):
        self.assertTrue(type(self.base1.id), str)
        self.assertEqual(len(self.base1.id), 36)

    def tearDown(self):
        pass

    def test_base_model_created_at(self):
        self.assertEqual(
            len(self.base1.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.base1.created_at), datetime)

    def test_base_model_updated_at(self):
        self.assertEqual(
            len(self.base1.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.base1.updated_at), datetime)

    def test_base_model_to_dict(self):
        self.assertTrue(type(self.base1.to_dict()), dict)

    def test_base_model_save(self):
        self.base1.save()
        self.assertEqual(
            len(self.base1.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.base1.updated_at), datetime)
