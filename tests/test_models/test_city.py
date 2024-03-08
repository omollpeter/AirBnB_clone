import unittest
from models.city import City
from models.state import State
from datetime import datetime


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city1 = City()
        self.city1.name = "City1"
        self.city1.contact = 40101
        dict1 = self.city1.to_dict()
        self.city2 = City(**dict1)
        dict2 = {}
        self.city3 = City(**dict2)
        self.city3.name = "City3"
        self.city3.contact = 40102
        self.state1 = State()
        self.state2 = State()

    def test_city_instance_id(self):
        self.assertTrue(type(self.city1.id), str)
        self.assertEqual(len(self.city1.id), 36)

        self.assertTrue(type(self.city2.id), str)
        self.assertEqual(len(self.city2.id), 36)

        self.assertTrue(type(self.city3.id), str)
        self.assertEqual(len(self.city3.id), 36)

    def tearDown(self):
        pass

    def test_city_created_at(self):
        self.assertEqual(
            len(self.city1.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.city1.created_at), datetime)

        self.assertEqual(
            len(self.city1.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.city1.created_at), datetime)

        self.assertEqual(
            len(self.city2.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.city2.created_at), datetime)

    def test_city_updated_at(self):
        self.assertEqual(
            len(self.city1.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.city1.updated_at), datetime)

        self.assertEqual(
            len(self.city2.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.city2.updated_at), datetime)

        self.assertEqual(
            len(self.city3.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.city3.updated_at), datetime)

    def test_city_to_dict(self):
        self.assertTrue(type(self.city1.to_dict()), dict)
        self.assertEqual(self.city1.to_dict()["name"], "City1")
        dict_ = self.city1.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

        self.city2 = City(**dict_)
        self.assertTrue(type(self.city2.to_dict()), dict)
        self.assertEqual(self.city2.to_dict()["name"], "City1")
        dict_ = self.city2.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

        self.assertTrue(type(self.city3.to_dict()), dict)
        self.assertEqual(self.city3.to_dict()["name"], "City3")
        dict_ = self.city3.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

    def test_city_save(self):
        self.city1.save()
        self.assertEqual(
            len(self.city1.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.city1.updated_at), datetime)

        self.city2.save()
        self.assertEqual(
            len(self.city2.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.city2.updated_at), datetime)

        self.city3.save()
        self.assertEqual(
            len(self.city3.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.city3.updated_at), datetime)

    def test_city_args(self):
        self.assertRaises(TypeError, City, {})
        self.assertRaises(TypeError, City, 1, 2)
        self.assertRaises(TypeError, City, "123", {}, 4)
        self.assertRaises(TypeError, City, None)
        self.assertRaises(TypeError, City, [])
        self.assertRaises(TypeError, City, 3.14159)
        self.assertRaises(TypeError, City, {1, 2, 3})
        self.assertRaises(TypeError, City, (1, 2, 3))

    def test_city_state_id(self):
        self.city1.state_id = self.state1.id
        self.city2.state_id = self.state2.id

        self.assertTrue(self.city1.state_id, self.state1.id)
        self.assertTrue(self.city2.state_id, self.state2.id)

    def test_city_name(self):
        self.city1.name = "Sansiro"
        self.city2.name = "Madrid"

        self.assertEqual(self.city1.name, "Sansiro")
        self.assertEqual(self.city2.name, "Madrid")
