#!/usr/bin/python3

import unittest
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    """Unit tests for the BaseModel class"""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        base_model = BaseModel()
        base_model.save()
        self.assertIn(base_model, models.storage.all().values())


if __name__ == '__main__':
    unittest.main()
