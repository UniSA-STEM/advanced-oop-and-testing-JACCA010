import unittest
from enclosure import Enclosure
from animal import Animal

# Mock child class for testing purposes only

class MockAnimal(Animal):
    def cry(self):
        return "Test cry"

    def move(self):
        return "Test move"

    def sleep(self):
        return "Test sleep"

class TestEnclosure(unittest.TestCase):

        def setUp(self):
            self.pond_small = Enclosure("Pond", "Small", "amphibian", 10)
            self.aviary_small = Enclosure("Aviary", "Small", "bird", 10)
            self.savannah_medium = Enclosure("Savannah", "Medium", "african savannah", 30)
            self.frog = MockAnimal("Kermit", "frog", "reptile", 2, "bugs", "Pond", "Ribbet")
            self.owl = MockAnimal("Hoobert", "Owl", "bird", 5, "Mice", "Aviary", "Hoot")
            self.zebra = MockAnimal("Stripez", "Zebra", "african savannah", 3, "assorted grasses", "Savannah", "Vocalise")

        def test_add_animal_and_summary(self):
            self.aviary_small.add_animal(self.owl)
            summary = self.aviary_small.summary()
            self.assertEqual(summary["Owl"], 1)
            self.assertNotIn("frog", summary)  # frog not added here

        def test_enclosure_capacity(self):
            self.assertEqual(self.aviary_small.enclosure_capacity(), "Empty")
            self.aviary_small.add_animal(self.owl)
            self.assertEqual(self.aviary_small.enclosure_capacity(), "Low (under 25%)")

        def test_upgrade_enclosure(self):
            # Fill aviary to capacity
            for i in range(10):
                self.aviary_small.add_animal(MockAnimal(f"Bird{i}", "Parrot", "bird", 1, "Seeds", "Aviary", "Squawk"))
            self.assertEqual(self.aviary_small.enclosure_capacity(), "Full")
            new_size = self.aviary_small.upgrade_enclosure()
            self.assertEqual(new_size, "Medium")

        def test_downgrade_enclosure(self):
            # Savannah starts Medium, only 1 zebra inside
            self.savannah_medium.add_animal(self.zebra)
            new_size = self.savannah_medium.downgrade_enclosure()
            self.assertEqual(new_size, "Small")

        def test_move_animals_success(self):
            self.aviary_small.add_animal(self.owl)
            moved = self.aviary_small.move_animals(self.owl, self.pond_small)
            self.assertTrue(moved)
            self.assertEqual(self.aviary_small.summary(), {})
            self.assertEqual(self.pond_small.summary()["Owl"], 1)

        def test_move_animals_incompatible_species(self):
            self.savannah_medium.add_animal(self.zebra)
            self.aviary_small.add_animal(self.owl)
            moved = self.aviary_small.move_animals(self.owl, self.savannah_medium)
            self.assertFalse(moved)


if __name__ == '__main__':
    unittest.main()
