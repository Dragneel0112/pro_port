#!/usr/bin/python3
"""
Contains the TestStateDocs classes
"""

from datetime import datetime
import inspect
import models
from models import plants
from models.base_model import BaseModel
import pep8
import unittest
Plants = plants.Plants


class TestStateDocs(unittest.TestCase):
    """Tests to check the documentation and style of Plants class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.plants_f = inspect.getmembers(Plants, inspect.isfunction)

    def test_pep8_conformance_plants(self):
        """Test that models/state.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/plants.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_Plants(self):
        """Test that tests/test_models/test_plants.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_plants.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_plant_module_docstring(self):
        """Test for the plants.py module docstring"""
        self.assertIsNot(Plants.__doc__, None,
                         "plants.py needs a docstring")
        self.assertTrue(len(Plants.__doc__) >= 1,
                        "plants.py needs a docstring")

    def test_plants_class_docstring(self):
        """Test for the Plants class docstring"""
        self.assertIsNot(Plants.__doc__, None,
                         "Plants class needs a docstring")
        self.assertTrue(len(Plants.__doc__) >= 1,
                        "Plants class needs a docstring")

    def test_Plants_func_docstrings(self):
        """Test for the presence of docstrings in Plant methods"""
        for func in self.plants_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestPlants(unittest.TestCase):
    """Test the State class"""
    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel"""
        plants = Plants()
        self.assertIsInstance(plants, BaseModel)
        self.assertTrue(hasattr(plants, "id"))
        self.assertTrue(hasattr(plants, "created_at"))
        self.assertTrue(hasattr(plants, "updated_at"))

    def test_name_attr(self):
        """Test that State has attribute name, and it's as an empty string"""
        plants = Plants()
        self.assertTrue(hasattr(plants, "name"))
        if models.storage_t == 'db':
            self.assertEqual(plants.name, None)
        else:
            self.assertEqual(plants.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        p = Plants()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in p.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Plants()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Plants")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        plants = Plants()
        string = "[Plants] ({}) {}".format(plants.id, plants.__dict__)
        self.assertEqual(string, str(plants))
