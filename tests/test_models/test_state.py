import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    def setUp(self):
        self.state1 = State()
        self.state1.name = "State1"
        self.state1.contact = 40101
        dict1 = self.state1.to_dict()
        self.state2 = State(**dict1)
        dict2 = {}
        self.state3 = State(**dict2)
        self.state3.name = "State3"
        self.state3.contact = 40102

    def test_state_instance_id(self):
        self.assertTrue(type(self.state1.id), str)
        self.assertEqual(len(self.state1.id), 36)

        self.assertTrue(type(self.state2.id), str)
        self.assertEqual(len(self.state2.id), 36)

        self.assertTrue(type(self.state3.id), str)
        self.assertEqual(len(self.state3.id), 36)

    def tearDown(self):
        pass

    def test_state_created_at(self):
        self.assertEqual(
            len(self.state1.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.state1.created_at), datetime)

        self.assertEqual(
            len(self.state1.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.state1.created_at), datetime)

        self.assertEqual(
            len(self.state2.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.state2.created_at), datetime)

    def test_state_updated_at(self):
        self.assertEqual(
            len(self.state1.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.state1.updated_at), datetime)

        self.assertEqual(
            len(self.state2.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.state2.updated_at), datetime)

        self.assertEqual(
            len(self.state3.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.state3.updated_at), datetime)

    def test_state_to_dict(self):
        self.assertTrue(type(self.state1.to_dict()), dict)
        self.assertEqual(self.state1.to_dict()["name"], "State1")
        dict_ = self.state1.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

        self.state2 = State(**dict_)
        self.assertTrue(type(self.state2.to_dict()), dict)
        self.assertEqual(self.state2.to_dict()["name"], "State1")
        dict_ = self.state2.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

        self.assertTrue(type(self.state3.to_dict()), dict)
        self.assertEqual(self.state3.to_dict()["name"], "State3")
        dict_ = self.state3.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

    def test_state_save(self):
        self.state1.save()
        self.assertEqual(
            len(self.state1.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.state1.updated_at), datetime)

        self.state2.save()
        self.assertEqual(
            len(self.state2.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.state2.updated_at), datetime)

        self.state3.save()
        self.assertEqual(
            len(self.state3.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.state3.updated_at), datetime)

    def test_state_args(self):
        self.assertRaises(TypeError, State, {})
        self.assertRaises(TypeError, State, 1, 2)
        self.assertRaises(TypeError, State, "123", {}, 4)
        self.assertRaises(TypeError, State, None)
        self.assertRaises(TypeError, State, [])
        self.assertRaises(TypeError, State, 3.14159)
        self.assertRaises(TypeError, State, {1, 2, 3})
        self.assertRaises(TypeError, State, (1, 2, 3))

    def test_state_name(self):
        self.state1.name = "Seattle"
        self.state2.name = "Oklohama"

        self.assertEqual(self.state1.name, "Seattle")
        self.assertEqual(self.state2.name, "Oklohama")
