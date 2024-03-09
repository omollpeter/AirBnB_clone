#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.user import User
from models.city import City
from models.amenity import Amenity

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

print("-- Create a new Place --")
my_place = Place()
my_city = City()
my_amen1 = Amenity()
my_amen2 = Amenity()
my_amen3 = Amenity()
my_place.name = "Minesota"
my_place.city_id = my_city.id
my_place.user_id = my_user.id
my_place.amenity_ids = [my_amen1.id, my_amen2.id, my_amen3.id]
my_place.description = "Beach"
my_place.number_rooms = 20
my_place.number_bathrooms = 20
my_place.max_guest = 40
my_place.price_by_night = 1945
my_place.latitude = 37.5
my_place.longitude = 22.67
my_place.dishes = {"African": ["ugali", "fish"], "Latin": ("tequila", "tacos")}
my_place.save()
print(my_place)
