'''
File: bird_test.py
Description: Test file for bird_test.
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''



import unittest
from bird import Bird

class TestBird(unittest.TestCase):

    def test_parrot_cry(self):
        bird = Bird(name="Polly", species="parrot", animal_group="avian", age=3,
                    dietary_requirement="seeds", enclosure="tropical", cry=None)
        self.assertIsNone(bird.cry())    # cry() prints output, doesn't return

    def test_duck_movement(self):
        bird = Bird(name="Daisy", species="duck", animal_group="avian", age=2,
                    dietary_requirement="plants", enclosure="pond", cry=None)
        bird.move()    # Should print "Daisy is flying!"

    def test_owl_sleep(self):
        bird = Bird(name="Hootie", species="owl", animal_group="avian", age=4,
                    dietary_requirement="mice", enclosure="forest", cry=None)
        bird.sleep()    # Should print "Hootie has perched for the day."

    def test_default_cry(self):
        bird = Bird(name="Chirpy", species=None, animal_group="avian", age=1,
                    dietary_requirement="fruit", enclosure="aviary", cry=None)
        bird.cry()    # Should print "Chirpy Chirrups!"

    def test_penguin_move(self):
        bird = Bird(name="Mr Waddles", species="penguin", animal_group="avian", age=1,
                    dietary_requirement="fish", enclosure="antartic", cry=None)
        bird.move()   # Should print "Mr Waddles is a flightless bird."

    def test_parrot_move(self):
        bird = Bird(name="Sunshine", species="parrot", animal_group="avian", age=5,
                    dietary_requirement="seeds", enclosure="aviary", cry=None)
        bird.move()  # Should print "Sunshine is flying!"

    def test_default_move(self):
        bird = Bird(name="Spicy", species=None, animal_group="avian", age=5,
                    dietary_requirement="seeds", enclosure="aviary", cry=None)
        bird.move()  # Should print "Spicy is flying!"

if __name__ == '__main__':
    unittest.main()