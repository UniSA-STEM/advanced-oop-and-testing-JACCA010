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
        latest = self.animal.latest_health_record()
        self.assertEqual(latest["status"], "Injured")
        self.assertEqual(latest["date"], "15-JUN-2025")
        self.assertIn("Minor paw cut", latest["notes"])

    def test_get_health_history(self):
        self.animal.add_health_record("07-MAY-2025", "Healthy", "Routine check-up")
        history = self.animal.get_health_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["status"], "Healthy")

    def test_str_output_with_health(self):
        self.animal.add_health_record("15-JUN-2025", "Injured", "Minor paw cut treated")
        output = str(self.animal)
        self.assertIn("Health Status: Injured", output)
        self.assertIn("15-JUN-2025", output)

if __name__ == "__main__":
    unittest.main()