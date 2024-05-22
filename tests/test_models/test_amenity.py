#!/usr/bin/python3
"""
unittests for models/amenity.py
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing instantiation and methods of the Amenity class."""

    def test_no_args_instantiates(self):
        """Test: No arguments instantiates the Amenity class."""
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        """Test: New instance is stored in objects."""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test: ID is a public string."""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        """Test: created_at is a public datetime."""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test: updated_at is a public datetime."""
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        """Test: name is a public class attribute."""
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_unique_ids(self):
        """Test: Two amenities have unique IDs."""
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_two_amenities_different_created_at(self):
        """Test: Two amenities have different created_at timestamps."""
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_two_amenities_different_updated_at(self):
        """Test: Two amenities have different updated_at timestamps."""
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_representation(self):
        """Test: String representation of the Amenity instance."""
        dt = datetime.today()
        dt_repr = repr(dt)
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        amstr = am.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_args_unused(self):
        """Test: Unused arguments are ignored."""
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test: Instantiation with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        am = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(am.id, "345")
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test: Instantiation with None keyword arguments raises TypeError."""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_save_method_updates_updated_at(self):
        """Test: save method updates updated_at attribute."""
        am = Amenity()
        old_updated_at = am.updated_at
        sleep(0.05)
        am.save()
        self.assertLess(old_updated_at, am.updated_at)

    def test_to_dict_creates_dict(self):
        """Test: to_dict method creates a dictionary with proper attrs."""
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(dict, type(am_dict))
        self.assertIn('id', am_dict)
        self.assertIn('created_at', am_dict)
        self.assertIn('updated_at', am_dict)
        self.assertIn('__class__', am_dict)

    def test_to_dict_values(self):
        """Test: to_dict method values are correct."""
        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        am_dict = am.to_dict()
        self.assertEqual(am_dict['id'], "123456")
        self.assertEqual(am_dict['created_at'], dt.isoformat())
        self.assertEqual(am_dict['updated_at'], dt.isoformat())
        self.assertEqual(am_dict['__class__'], 'Amenity')

    def test_to_dict_with_extra_attributes(self):
        """Test: to_dict method includes extra attributes."""
        am = Amenity()
        am.middle_name = "Middle"
        am.my_number = 42
        am_dict = am.to_dict()
        self.assertEqual(am_dict['middle_name'], "Middle")
        self.assertEqual(am_dict['my_number'], 42)


if __name__ == "__main__":
    unittest.main()
