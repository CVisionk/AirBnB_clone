#!/usr/bin/python3
"""
unittests for models/place.py
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittests for testing instantiation and methods of the Place class."""

    def test_no_args_instantiates(self):
        """Test: No arguments instantiates the Place class."""
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        """Test: New instance is stored in objects."""
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test: ID is a public string."""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        """Test: created_at is a public datetime."""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test: updated_at is a public datetime."""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        """Test: city_id is a public class attribute."""
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_user_id_is_public_class_attribute(self):
        """Test: user_id is a public class attribute."""
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    def test_name_is_public_class_attribute(self):
        """Test: name is a public class attribute."""
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    def test_description_is_public_class_attribute(self):
        """Test: description is a public class attribute."""
        pl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pl))
        self.assertNotIn("description", pl.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        """Test: number_rooms is a public class attribute."""
        pl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        """Test: number_bathrooms is a public class attribute."""
        pl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        """Test: max_guest is a public class attribute."""
        pl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        """Test: price_by_night is a public class attribute."""
        pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

    def test_latitude_is_public_class_attribute(self):
        """Test: latitude is a public class attribute."""
        pl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pl))
        self.assertNotIn("latitude", pl.__dict__)

    def test_longitude_is_public_class_attribute(self):
        """Test: longitude is a public class attribute."""
        pl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pl))
        self.assertNotIn("longitude", pl.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        """Test: amenity_ids is a public class attribute."""
        pl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)

    def test_two_places_unique_ids(self):
        """Test: Two places have unique IDs."""
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_two_places_different_created_at(self):
        """Test: Two places have different created_at timestamps."""
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_two_places_different_updated_at(self):
        """Test: Two places have different updated_at timestamps."""
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def test_str_representation(self):
        """Test: String representation of the Place instance."""
        dt = datetime.today()
        dt_repr = repr(dt)
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        plstr = pl.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

    def test_args_unused(self):
        """Test: Unused arguments are ignored."""
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test: Instantiation with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        pl = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(pl.id, "345")
        self.assertEqual(pl.created_at, dt)
        self.assertEqual(pl.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test: Instantiation with None keyword arguments raises TypeError."""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_save_method_updates_updated_at(self):
        """Test: save method updates updated_at attribute."""
        pl = Place()
        old_updated_at = pl.updated_at
        sleep(0.05)
        pl.save()
        self.assertLess(old_updated_at, pl.updated_at)

    def test_to_dict_creates_dict(self):
        """Test: to_dict method creates a dictionary with proper attrs."""
        pl = Place()
        pl_dict = pl.to_dict()
        self.assertEqual(dict, type(pl_dict))
        self.assertIn('id', pl_dict)
        self.assertIn('created_at', pl_dict)
        self.assertIn('updated_at', pl_dict)
        self.assertIn('__class__', pl_dict)

    def test_to_dict_values(self):
        """Test: to_dict method values are correct."""
        dt = datetime.today()
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        pl_dict = pl.to_dict()
        self.assertEqual(pl_dict['id'], "123456")
        self.assertEqual(pl_dict['created_at'], dt.isoformat())
        self.assertEqual(pl_dict['updated_at'], dt.isoformat())
        self.assertEqual(pl_dict['__class__'], 'Place')

    def test_to_dict_with_extra_attributes(self):
        """Test: to_dict method includes extra attributes."""
        pl = Place()
        pl.middle_name = "Middle"
        pl.my_number = 42
        pl_dict = pl.to_dict()
        self.assertEqual(pl_dict['middle_name'], "Middle")
        self.assertEqual(pl_dict['my_number'], 42)


if __name__ == "__main__":
    unittest.main()
