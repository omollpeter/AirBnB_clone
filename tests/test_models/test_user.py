import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user1 = User()
        self.user1.name = "User1"
        self.user1.contact = 40101
        dict1 = self.user1.to_dict()
        self.user2 = User(**dict1)
        dict2 = {}
        self.user3 = User(**dict2)
        self.user3.name = "User3"
        self.user3.contact = 40102

    def test_user_instance_id(self):
        self.assertTrue(type(self.user1.id), str)
        self.assertEqual(len(self.user1.id), 36)

        self.assertTrue(type(self.user2.id), str)
        self.assertEqual(len(self.user2.id), 36)

        self.assertTrue(type(self.user3.id), str)
        self.assertEqual(len(self.user3.id), 36)

    def tearDown(self):
        pass

    def test_user_created_at(self):
        self.assertEqual(
            len(self.user1.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.user1.created_at), datetime)

        self.assertEqual(
            len(self.user1.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.user1.created_at), datetime)

        self.assertEqual(
            len(self.user2.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.user2.created_at), datetime)

    def test_user_updated_at(self):
        self.assertEqual(
            len(self.user1.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.user1.updated_at), datetime)

        self.assertEqual(
            len(self.user2.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.user2.updated_at), datetime)

        self.assertEqual(
            len(self.user3.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.user3.updated_at), datetime)

    def test_user_to_dict(self):
        self.assertTrue(type(self.user1.to_dict()), dict)
        self.assertEqual(self.user1.to_dict()["name"], "User1")
        dict_ = self.user1.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

        self.user2 = User(**dict_)
        self.assertTrue(type(self.user2.to_dict()), dict)
        self.assertEqual(self.user2.to_dict()["name"], "User1")
        dict_ = self.user2.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

        self.assertTrue(type(self.user3.to_dict()), dict)
        self.assertEqual(self.user3.to_dict()["name"], "User3")
        dict_ = self.user3.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

    def test_user_save(self):
        self.user1.save()
        self.assertEqual(
            len(self.user1.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.user1.updated_at), datetime)

        self.user2.save()
        self.assertEqual(
            len(self.user2.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.user2.updated_at), datetime)

        self.user3.save()
        self.assertEqual(
            len(self.user3.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.user3.updated_at), datetime)

    def test_user_args(self):
        self.assertRaises(TypeError, User, {})
        self.assertRaises(TypeError, User, 1, 2)
        self.assertRaises(TypeError, User, "123", {}, 4)
        self.assertRaises(TypeError, User, None)
        self.assertRaises(TypeError, User, [])
        self.assertRaises(TypeError, User, 3.14159)
        self.assertRaises(TypeError, User, {1, 2, 3})
        self.assertRaises(TypeError, User, (1, 2, 3))

    def test_user_email(self):
        self.user1.email = "airbnb@mail.com"
        self.user2.email = "airbnb2@mail.com"
        self.user3.email = "airbnb3@mail.com"

        self.assertEqual(self.user1.email, "airbnb@mail.com")
        self.assertEqual(self.user2.email, "airbnb2@mail.com")
        self.assertEqual(self.user3.email, "airbnb3@mail.com")

    def test_user_password(self):
        self.user1.password = "root1"
        self.user2.password = "root2"
        self.user3.password = "root3"

        self.assertEqual(self.user1.password, "root1")
        self.assertEqual(self.user2.password, "root2")
        self.assertEqual(self.user3.password, "root3")

    def test_user_first_name(self):
        self.user1.first_name = "Peter"
        self.user2.first_name = "John"

        self.assertEqual(self.user1.first_name, "Peter")
        self.assertEqual(self.user2.first_name, "John")

    def test_user_last_name(self):
        self.user1.last_name = "Omollo"
        self.user2.last_name = "Ndege"

        self.assertEqual(self.user1.last_name, "Omollo")
        self.assertEqual(self.user2.last_name, "Ndege")
