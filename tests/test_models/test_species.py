#!/usr/bin/python3
"""
Contains the TestCityDocs classes
"""

from datetime import datetime
import inspect
import models
from models import species
from models.base_model import BaseModel
import pep8
import unittest
Species = species.Species


class TestSpeciesDocs(unittest.TestCase):
    """Tests to check the documentation and style of Species class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.Species_f = inspect.getmembers(Species, inspect.isfunction)

    def test_pep8_conformance_Species(self):
        """Test that models/species.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/species.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_species(self):
        """Test that tests/test_models/test_species.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_species.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_species_module_docstring(self):
        """Test for the species.py module docstring"""
        self.assertIsNot(Species.__doc__, None,
                         "species.py needs a docstring")
        self.assertTrue(len(Species.__doc__) >= 1,
                        "species.py needs a docstring")

    def test_species_class_docstring(self):
        """Test for the Species class docstring"""
        self.assertIsNot(Species.__doc__, None,
                         "Species class needs a docstring")
        self.assertTrue(len(Species.__doc__) >= 1,
                        "Species class needs a docstring")

    def test_Species_func_docstrings(self):
        """Test for the presence of docstrings in Species methods"""
        for func in self.Species_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestSpecies(unittest.TestCase):
    """Test the Species class"""
    def test_is_subclass(self):
        """Test that Species is a subclass of BaseModel"""
        species = Species()
        self.assertIsInstance(species, BaseModel)
        self.assertTrue(hasattr(species, "id"))
        self.assertTrue(hasattr(species, "created_at"))
        self.assertTrue(hasattr(species, "updated_at"))

    def test_name_attr(self):
        """Test that Species has attribute name, and it's an empty string"""
        species = Species()
        self.assertTrue(hasattr(species, "name"))
        if models.storage_t == 'db':
            self.assertEqual(species.name, None)
        else:
            self.assertEqual(species.name, "")

    def test_Plant_id_attr(self):
        """Test that Species has attribute plant_id, empty string"""
        species = Species()
        self.assertTrue(hasattr(species, "plant_id"))
        if models.storage_t == 'db':
            self.assertEqual(species.plant_id, None)
        else:
            self.assertEqual(species.plant_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        s = Species()
        new_d = s.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in s.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = Species()
        new_d = s.to_dict()
        self.assertEqual(new_d["__class__"], "Species")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], s.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        species = Species()
        string = "[Species] ({}) {}".format(species.id, species.__dict__)
        self.assertEqual(string, str(species))
