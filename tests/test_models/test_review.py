#!/usr/bin/python3
"""
unittests for models/review.py
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittests for testing instantiation and methods of the Review class."""

    def test_no_args_instantiates(self):
        """Test: No arguments instantiates the Review class."""
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        """Test: New instance is stored in objects."""
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test: ID is a public string."""
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        """Test: created_at is a public datetime."""
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test: updated_at is a public datetime."""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        """Test: place_id is a public class attribute."""
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_public_class_attribute(self):
        """Test: user_id is a public class attribute."""
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_public_class_attribute(self):
        """Test: text is a public class attribute."""
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_two_reviews_unique_ids(self):
        """Test: Two reviews have unique IDs."""
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_two_reviews_different_created_at(self):
        """Test: Two reviews have different created_at timestamps."""
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_two_reviews_different_updated_at(self):
        """Test: Two reviews have different updated_at timestamps."""
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_str_representation(self):
        """Test: String representation of the Review instance."""
        dt = datetime.today()
        dt_repr = repr(dt)
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        rvstr = rv.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

    def test_args_unused(self):
        """Test: Unused arguments are ignored."""
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test: Instantiation with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "345")
        self.assertEqual(rv.created_at, dt)
        self.assertEqual(rv.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test: Instantiation with None keyword arguments raises TypeError."""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_save_method_updates_updated_at(self):
        """Test: save method updates updated_at attribute."""
        rv = Review()
        old_updated_at = rv.updated_at
        sleep(0.05)
        rv.save()
        self.assertLess(old_updated_at, rv.updated_at)

    def test_to_dict_creates_dict(self):
        """Test: to_dict method creates a dictionary with proper attrs."""
        rv = Review()
        rv_dict = rv.to_dict()
        self.assertEqual(dict, type(rv_dict))
        self.assertIn('id', rv_dict)
        self.assertIn('created_at', rv_dict)
        self.assertIn('updated_at', rv_dict)
        self.assertIn('__class__', rv_dict)

    def test_to_dict_values(self):
        """Test: to_dict method values are correct."""
        dt = datetime.today()
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        rv_dict = rv.to_dict()
        self.assertEqual(rv_dict['id'], "123456")
        self.assertEqual(rv_dict['created_at'], dt.isoformat())
        self.assertEqual(rv_dict['updated_at'], dt.isoformat())
        self.assertEqual(rv_dict['__class__'], 'Review')

    def test_to_dict_with_extra_attributes(self):
        """Test: to_dict method includes extra attributes."""
        rv = Review()
        rv.middle_name = "Middle"
        rv.my_number = 42
        rv_dict = rv.to_dict()
        self.assertEqual(rv_dict['middle_name'], "Middle")
        self.assertEqual(rv_dict['my_number'], 42)


if __name__ == "__main__":
    unittest.main()
