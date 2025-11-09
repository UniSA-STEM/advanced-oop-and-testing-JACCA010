import unittest

from animal import Animal

# Mock child class for testing purposes only

class MockAnimal(Animal):
    def cry(self):
        return "Test cry"

    def move(self):
        return "Test move"

    def sleep(self):
        return "Test sleep"

class TestAnimalClass(unittest.TestCase):

    def setUp(self):
        self.animal = MockAnimal(
            name="Sample",
            species="SampleSpecies",
            animal_group="SampleGroup",
            age=5,
            dietary_requirement="SampleFood",
            enclosure="SampleEnclosure",
            cry="SampleCry"
        )

    def test_unique_id(self):
        id1 = self.animal.get_animal_id()
        id2 = MockAnimal("A", "B", "C", 1, "D", "E","AnotherCry").get_animal_id()
        self.assertNotEqual(id1, id2)

    def test_getters(self):
        self.assertEqual(self.animal.get_name(), "Sample")
        self.assertEqual(self.animal.get_species(), "SampleSpecies")
        self.assertEqual(self.animal.get_enclosure(), "SampleEnclosure")

    def test_enclosure_status_initial(self):
        self.assertEqual(self.animal._Animal__enclosure_status, 3)

    def test_eat(self):
        self.animal.eat()
        self.assertEqual(self.animal.get_enclosure_status(), 2)

    def test_str_output(self):
        self.assertIn("Sample", str(self.animal))
        self.assertIn("SampleEnclosure", str(self.animal))

if __name__ == "__main__":
    unittest.main()