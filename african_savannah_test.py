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

class TestAfrican_Savannah(unittest.TestCase):

    def test_lion_cry(self):
        african_savannah = African_Savannah(name="Sleepy", species="tortoise", animal_group="reptile", age=32,
                    dietary_requirement="green leaves", enclosure="pond", cry=None)
        reptile.cry()    # Should print "Sleepy Puffs!"

    def test_tortoise_cry(self):
        reptile = Reptile(name="Sleepy", species=None, animal_group="reptile", age=32,
                    dietary_requirement="green leaves", enclosure="pond", cry=None)
        self.assertIsNone(reptile.cry())    # cry() prints output, doesn't return

    def test_frog_cry(self):
        reptile = Reptile(name="Prince Toadie", species="frog", animal_group="reptile", age=2,
                    dietary_requirement="green leaves", enclosure="pond", cry=None)
        reptile.cry()    # Should print "Prince Toadie Ribbets!"

    def test_crocodile_movement(self):
        reptile = Reptile(name="Roger", species="crocodile", animal_group="reptile", age=10,
                    dietary_requirement="carnivore", enclosure="pond", cry=None)
        reptile.move()    # Should print "Roger is stalking."

    def test_snake_sleep(self):
        reptile = Reptile(name="Simon", species="snake", animal_group="reptile", age=4,
                    dietary_requirement="mice", enclosure="rock bed", cry=None)
        reptile.sleep()    # Should print "Simon has coiled up and is sleeping."

    if species not in self.african_species_dict:
        raise ValueError(f"{species} is not recognized as an African savannah species.")


if __name__ == '__main__':
    unittest.main()
