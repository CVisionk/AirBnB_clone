#!/usr/bin/python3
"""
unittests for models/city
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_city(self):
        """Test: No arguments instantiates the City class."""
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """Test: New instance is stored in objects."""
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test: ID is a public string."""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """Test: created_at is a public datetime."""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test: updated_at is a public datetime."""
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        """Test: state_id is a public class attribute."""
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_public_class_attribute(self):
        """Test: name is a public class attribute."""
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_two_cities_unique_ids(self):
        """Test: Two cities have unique IDs."""
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_cities_different_created_at(self):
        """Test: Two cities have different created_at timestamps."""
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_cities_different_updated_at(self):
        """Test: Two cities have different updated_at timestamps."""
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_str_representation(self):
        """Test: String representation of the City instance."""
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cystr = cy.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_args_unused(self):
        """Test: Unused arguments are ignored."""
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test: Instantiation with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cy = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(cy.id, "345")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test: Instantiation with None keyword arguments raises TypeError."""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setUp(self):
        """Set up the test environment by renaming file.json if it exists."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Clean up the test environment by removing and renaming files."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test: save method updates the updated_at attribute."""
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        self.assertLess(first_updated_at, cy.updated_at)

    def test_two_saves(self):
        """Test: Multiple saves update the updated_at attribute."""
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        second_updated_at = cy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cy.save()
        self.assertLess(second_updated_at, cy.updated_at)

    def test_save_with_arg(self):
        """Test: save method with arguments raises TypeError."""
        cy = City()
        with self.assertRaises(TypeError):
            cy.save(None)

    def test_save_updates_file(self):
        """Test: save method updates file.json."""
        cy = City()
        cy.save()
        cyid = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        """Test: to_dict method creates a dictionary."""
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test: to_dict method contains correct keys."""
        cy = City()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test: to_dict method includes added attributes."""
        cy = City()
        cy.middle_name = "Holberton"
        cy.my_number = 98
        self.assertEqual("Holberton", cy.middle_name)
        self.assertIn("my_number", cy.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test: to_dict method converts datetime attributes to strings."""
        cy = City()
        cy_dict = cy.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test: to_dict method output is as expected."""
        dt = datetime.today()
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cy.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test: to_dict method differs from __dict__ method."""
        cy = City()
        self.assertNotEqual(cy.to_dict(), cy.__dict__)

    def test_to_dict_with_arg(self):
        """Test: to_dict method with arguments raises TypeError."""
        cy = City()
        with self.assertRaises(TypeError):
            cy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
