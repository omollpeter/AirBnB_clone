import unittest
from models.review import Review
from models.place import Place
from models.user import User
from datetime import datetime


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review1 = Review()
        self.review1.name = "Review1"
        self.review1.contact = 40101
        dict1 = self.review1.to_dict()
        self.review2 = Review(**dict1)
        dict2 = {}
        self.review3 = Review(**dict2)
        self.review3.name = "Review3"
        self.review3.contact = 40102
        self.place1 = Place()
        self.place2 = Place()
        self.user1 = User()
        self.user2 = User()

    def test_review_instance_id(self):
        self.assertTrue(type(self.review1.id), str)
        self.assertEqual(len(self.review1.id), 36)

        self.assertTrue(type(self.review2.id), str)
        self.assertEqual(len(self.review2.id), 36)

        self.assertTrue(type(self.review3.id), str)
        self.assertEqual(len(self.review3.id), 36)

    def tearDown(self):
        pass

    def test_review_created_at(self):
        self.assertEqual(
            len(self.review1.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.review1.created_at), datetime)

        self.assertEqual(
            len(self.review1.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.review1.created_at), datetime)

        self.assertEqual(
            len(self.review2.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.review2.created_at), datetime)

    def test_review_updated_at(self):
        self.assertEqual(
            len(self.review1.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.review1.updated_at), datetime)

        self.assertEqual(
            len(self.review2.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.review2.updated_at), datetime)

        self.assertEqual(
            len(self.review3.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.review3.updated_at), datetime)

    def test_review_to_dict(self):
        self.assertTrue(type(self.review1.to_dict()), dict)
        self.assertEqual(self.review1.to_dict()["name"], "Review1")
        dict_ = self.review1.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

        self.review2 = Review(**dict_)
        self.assertTrue(type(self.review2.to_dict()), dict)
        self.assertEqual(self.review2.to_dict()["name"], "Review1")
        dict_ = self.review2.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

        self.assertTrue(type(self.review3.to_dict()), dict)
        self.assertEqual(self.review3.to_dict()["name"], "Review3")
        dict_ = self.review3.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

    def test_review_save(self):
        self.review1.save()
        self.assertEqual(
            len(self.review1.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.review1.updated_at), datetime)

        self.review2.save()
        self.assertEqual(
            len(self.review2.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.review2.updated_at), datetime)

        self.review3.save()
        self.assertEqual(
            len(self.review3.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.review3.updated_at), datetime)

    def test_review_args(self):
        self.assertRaises(TypeError, Review, {})
        self.assertRaises(TypeError, Review, 1, 2)
        self.assertRaises(TypeError, Review, "123", {}, 4)
        self.assertRaises(TypeError, Review, None)
        self.assertRaises(TypeError, Review, [])
        self.assertRaises(TypeError, Review, 3.14159)
        self.assertRaises(TypeError, Review, {1, 2, 3})
        self.assertRaises(TypeError, Review, (1, 2, 3))

    def test_review_place_id(self):
        self.review1.place_id = self.place1.id
        self.review2.place_id = self.place2.id

        self.assertTrue(self.review1.place_id, self.place1.id)
        self.assertTrue(self.review2.place_id, self.place2.id)

    def test_review_user_id(self):
        self.review1.user_id = self.user1.id
        self.review2.user_id = self.user2.id

        self.assertTrue(self.review1.user_id, self.user1.id)
        self.assertTrue(self.review2.user_id, self.user2.id)

    def test_review_text(self):
        self.review1.text = "The place was really cool"
        self.review2.text = "This place is awesome. It has a nice view"

        self.assertEqual(self.review1.text, "The place was really cool")
        self.assertEqual(
            self.review2.text,
            "This place is awesome. It has a nice view"
        )
