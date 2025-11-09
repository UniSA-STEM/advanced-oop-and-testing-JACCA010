import unittest
from zoo import Zoo
from animal import Animal

# Mock child class for testing purposes only (reusing mock child class from previous test)
class MockAnimal(Animal):
    def cry(self): return "Test cry"
    def move(self): return "Test move"
    def sleep(self): return "Test sleep"

class TestZooClass(unittest.TestCase):

    def setUp(self):
        self.zoo = Zoo("Cats Zoo")
        self.animal1 = MockAnimal("Leo", "Lion", "African Savannah", 4, "Meat", "Savannah", "Roar")
        self.animal2 = MockAnimal("Polly", "Parrot", "Avian", 2, "Seeds", "Aviary", "Squawk")

    def test_add_animal(self):
        self.zoo.add_animal(self.animal1)
        self.assertIn(self.animal1, self.zoo.animals)

    def test_add_non_animal(self):
        self.zoo.add_animal("NotAnAnimal")
        self.assertEqual(len(self.zoo.animals), 0)

    def test_remove_animal_by_id(self):
        self.zoo.add_animal(self.animal1)
        self.zoo.add_animal(self.animal2)
        self.zoo.remove_animal_by_id(self.animal1.get_animal_id())
        self.assertNotIn(self.animal1, self.zoo.animals)
        self.assertIn(self.animal2, self.zoo.animals)

    def test_remove_invalid_id(self):
        self.zoo.add_animal(self.animal1)
        self.zoo.remove_animal_by_id(999)  # ID that doesn't exist
        self.assertIn(self.animal1, self.zoo.animals)

    def test_list_animals_output(self):
        self.zoo.add_animal(self.animal1)
        self.zoo.add_animal(self.animal2)
        expected = (
            f"Animals in Cats Zoo:\n"
            f"- [ID {self.animal1.get_animal_id()}]\n"
            f"  Name: Leo\n"
            f"  Species: Lion\n"
            f"  Animal Group: African Savannah\n"
            f"- [ID {self.animal2.get_animal_id()}]\n"
            f"  Name: Polly\n"
            f"  Species: Parrot\n"
            f"  Animal Group: Avian"
        )
        self.assertEqual(str(self.zoo), expected)

if __name__ == "__main__":
    unittest.main()