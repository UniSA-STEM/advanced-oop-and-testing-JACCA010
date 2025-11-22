'''
File: animal_test.py
Description: Test file for animal_class.
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''


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

    def test_clean_enclosure(self):
        self.animal.eat()
        self.assertEqual(self.animal.get_enclosure_status(), 2)
        self.animal.clean_enclosure()
        self.assertEqual(self.animal.get_enclosure_status(), 3)

    def test_add_health_record_and_latest(self):
        self.animal.add_health_record("01-DEC-2025", "Healthy", "Routine check-up")
        self.animal.add_health_record("15-JUN-2025", "Injured", "Minor paw cut treated")
        latest = self.animal.latest_health_record_str()
        self.assertIn("Status: Injured", latest)
        self.assertIn("15-JUN-2025", latest)
        self.assertIn("Minor paw cut", latest)

    def test_get_health_history(self):
        self.animal.add_health_record("07-MAY-2025", "Healthy", "Routine check-up")
        history = self.animal.get_health_history_str()
        self.assertEqual(len(history), 1)
        self.assertIn("Status: Healthy", history[0])

    def test_str_output_with_health(self):
        self.animal.add_health_record("15-JUN-2025", "Injured", "Minor paw cut treated")
        output = str(self.animal)
        self.assertIn("Status: Injured", output)
        self.assertIn("15-JUN-2025", output)

    def test_add_animal(self):
        # Reset registry to as this is a standalone test
        Animal._register = []

        # Create two animals
        a1 = MockAnimal("George", "Lion", "african savannah", 5, "meat", "Savannah", "Roar")
        a2 = MockAnimal("Simba", "Lion", "african savannah", 4, "meat", "Savannah", "Roar")

        # Registry should contain both animals
        self.assertIn(a1, Animal.get_all_animals())
        self.assertIn(a2, Animal.get_all_animals())

        # animal should not duplicate
        Animal.add_animal(a1)
        count = Animal.get_all_animals().count(a1)
        self.assertEqual(count, 1)  # still only one instance

        # Remove one animal
        Animal.remove_animal(a1)
        self.assertNotIn(a1, Animal.get_all_animals())
        self.assertIn(a2, Animal.get_all_animals())


if __name__ == "__main__":
    unittest.main()