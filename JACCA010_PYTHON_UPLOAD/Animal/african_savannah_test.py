'''
File: african_savannah_test.py
Description: Special African Savannah test file to incorporate dictionary
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

import unittest
from african_savannah import African_Savannah

class TestAfricanSavannah(unittest.TestCase):

    def setUp(self):
        self.lion = African_Savannah("Simba", "lion", "mammal", 5, "carnivore", "Savannah 1", "Roar")
        self.elephant = African_Savannah("Dumbo", "elephant", "mammal", 10, "herbivore", "Savannah 2", "Trumpet")
        self.gazelle = African_Savannah("Grace", "gazelle", "mammal", 3, "herbivore", "Savannah 3", "Vocalise")

    def test_valid_species_instantiation(self):
        self.assertEqual(self.lion.get_species(), "lion")
        self.assertEqual(self.elephant.get_species(), "elephant")

    def test_invalid_species_raises_error(self):
        with self.assertRaises(ValueError):
            African_Savannah("Tony", "tiger", "mammal", 4, "carnivore", "Savannah X", "Roar")

    def test_cry_behavior(self):
        self.assertEqual(self.lion.cry(), "Simba Roars!")
        self.assertEqual(self.elephant.cry(), "Dumbo Trumpets!")
        self.assertEqual(self.gazelle.cry(), "Grace Vocalises!")

    def test_move_behavior(self):
        self.assertEqual(self.lion.move(), "Simba is stalking!")
        self.assertEqual(self.gazelle.move(), "Grace is leaping!")
        self.assertEqual(self.elephant.move(), "Dumbo is swaying!")

    def test_str_method(self):
        expected = "Simba the lion lives in enclosure Savannah 1 and cries 'Roar'."
        self.assertEqual(str(self.lion), expected)

if __name__ == "__main__":
    unittest.main()