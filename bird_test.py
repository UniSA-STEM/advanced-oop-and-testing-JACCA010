import unittest
from bird import Bird

if __name__ == '__main__':
    unittest.main()



class TestBird(unittest.TestCase):

    def test_parrot_cry(self):
        bird = Bird(name="Polly", species="parrot", animal_group="avian", age=3,
                    dietary_requirement="seeds", enclosure="tropical", cry=None)
        self.assertIsNone(bird.cry())  # cry() prints output, doesn't return

    def test_duck_movement(self):
        bird = Bird(name="Daisy", species="duck", animal_group="avian", age=2,
                    dietary_requirement="plants", enclosure="pond", cry=None)
        bird.move()  # Should print "Daisy is flapping its wings!"

    def test_owl_sleep(self):
        bird = Bird(name="Hootie", species="owl", animal_group="avian", age=4,
                    dietary_requirement="mice", enclosure="forest", cry=None)
        bird.sleep()  # Should print "Hootie has perched for the day."

    def test_default_cry(self):
        bird = Bird(name="Chirpy", species=None, animal_group="avian", age=1,
                    dietary_requirement="fruit", enclosure="aviary", cry=None)
        bird.cry()  # Should print "Chirpy Chirrups!"
