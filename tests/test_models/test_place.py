import unittest
from models.place import Place
from models.city import City
from models.user import User
from datetime import datetime
from models.amenity import Amenity


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place1 = Place()
        self.place1.name = "Place1"
        self.place1.contact = 40101
        dict1 = self.place1.to_dict()
        self.place2 = Place(**dict1)
        dict2 = {}
        self.place3 = Place(**dict2)
        self.place3.name = "Place3"
        self.place3.contact = 40102
        self.city1 = City()
        self.city2 = City()
        self.user1 = User()
        self.user2 = User()
        self.amenity1 = Amenity()
        self.amenity2 = Amenity()
        self.amenity3 = Amenity()

    def test_place_instance_id(self):
        self.assertTrue(type(self.place1.id), str)
        self.assertEqual(len(self.place1.id), 36)

        self.assertTrue(type(self.place2.id), str)
        self.assertEqual(len(self.place2.id), 36)

        self.assertTrue(type(self.place3.id), str)
        self.assertEqual(len(self.place3.id), 36)

    def tearDown(self):
        pass

    def test_place_created_at(self):
        self.assertEqual(
            len(self.place1.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.place1.created_at), datetime)

        self.assertEqual(
            len(self.place1.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.place1.created_at), datetime)

        self.assertEqual(
            len(self.place2.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.place2.created_at), datetime)

    def test_place_updated_at(self):
        self.assertEqual(
            len(self.place1.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.place1.updated_at), datetime)

        self.assertEqual(
            len(self.place2.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.place2.updated_at), datetime)

        self.assertEqual(
            len(self.place3.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.place3.updated_at), datetime)

    def test_place_to_dict(self):
        self.assertTrue(type(self.place1.to_dict()), dict)
        self.assertEqual(self.place1.to_dict()["name"], "Place1")
        dict_ = self.place1.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

        self.place2 = Place(**dict_)
        self.assertTrue(type(self.place2.to_dict()), dict)
        self.assertEqual(self.place2.to_dict()["name"], "Place1")
        dict_ = self.place2.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

        self.assertTrue(type(self.place3.to_dict()), dict)
        self.assertEqual(self.place3.to_dict()["name"], "Place3")
        dict_ = self.place3.to_dict()
        self.assertEqual(len(dict_["created_at"]), 26)
        self.assertEqual(len(dict_["updated_at"]), 26)
        self.assertTrue(type(dict_["created_at"]), str)
        self.assertTrue(type(dict_["updated_at"]), str)
        self.assertTrue(type(dict_["name"]), str)
        self.assertTrue(type(dict_["contact"]), int)

    def test_place_save(self):
        self.place1.save()
        self.assertEqual(
            len(self.place1.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.place1.updated_at), datetime)

        self.place2.save()
        self.assertEqual(
            len(self.place2.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.place2.updated_at), datetime)

        self.place3.save()
        self.assertEqual(
            len(self.place3.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f")),
            26
        )
        self.assertTrue(type(self.place3.updated_at), datetime)

    def test_place_args(self):
        self.assertRaises(TypeError, Place, {})
        self.assertRaises(TypeError, Place, 1, 2)
        self.assertRaises(TypeError, Place, "123", {}, 4)
        self.assertRaises(TypeError, Place, None)
        self.assertRaises(TypeError, Place, [])
        self.assertRaises(TypeError, Place, 3.14159)
        self.assertRaises(TypeError, Place, {1, 2, 3})
        self.assertRaises(TypeError, Place, (1, 2, 3))

    def test_place_city_id(self):
        self.place1.city_id = self.city1.id
        self.place2.city_id = self.city2.id

        self.assertTrue(self.place1.city_id, self.city1.id)
        self.assertTrue(self.place2.city_id, self.city2.id)

    def test_place_user_id(self):
        self.place1.user_id = self.user2.id
        self.place2.user_id = self.user1.id

        self.assertTrue(self.place2.user_id, self.user1.id)
        self.assertTrue(self.place1.user_id, self.user2.id)

    def test_place_name(self):
        self.place1.name = "Minesota"
        self.place2.name = "Jericho"

        self.assertEqual(self.place1.name, "Minesota")
        self.assertEqual(self.place2.name, "Jericho")

    def test_place_description(self):
        self.place1.description = "Beach"
        self.place2.description = "Desert"

        self.assertEqual(self.place1.description, "Beach")
        self.assertEqual(self.place2.description, "Desert")
    
    def test_place_number_rooms(self):
        self.place1.number_rooms = 10
        self.place2.number_rooms = 15

        self.assertEqual(self.place1.number_rooms, 10)
        self.assertEqual(self.place2.number_rooms, 15)

    def test_place_number_bathrooms(self):
        self.place1.number_bathrooms = 10
        self.place2.number_bathrooms = 15

        self.assertEqual(self.place1.number_bathrooms, 10)
        self.assertEqual(self.place2.number_bathrooms, 15)

    def test_place_max_guest(self):
        self.place1.max_guest = 100
        self.place2.max_guest = 150

        self.assertEqual(self.place1.max_guest, 100)
        self.assertEqual(self.place2.max_guest, 150)

    def test_place_price_by_night(self):
        self.place1.price_by_night = 5000
        self.place2.price_by_night = 2700

        self.assertEqual(self.place1.price_by_night, 5000)
        self.assertEqual(self.place2.price_by_night, 2700)

    def test_place_latitude(self):
        self.place1.latitude = 37.52
        self.place2.latitude = 22.06

        self.assertEqual(self.place1.latitude, 37.52)
        self.assertEqual(self.place2.latitude, 22.06)

    def test_place_longitude(self):
        self.place1.longitude = 37.52
        self.place2.longitude = 22.06

        self.assertEqual(self.place1.longitude, 37.52)
        self.assertEqual(self.place2.longitude, 22.06)

    def test_place_amenity_ids(self):
        self.place1.amenity_ids = [self.amenity1.id, self.amenity2.id]
        self.place2.amenity_ids = [self.amenity3.id]

        self.assertEqual(
            sorted(self.place1.amenity_ids),
            sorted([self.amenity1.id, self.amenity2.id])
        )
        self.assertEqual(
            sorted(self.place2.amenity_ids),
            sorted([self.amenity3.id])
        )
