'''
File: animal_test.py
Description: Test file for animal_class.
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''


import pytest
from animal import Animal

# Mock child class for testing purposes only
class MockAnimal(Animal):
    def cry(self):
        return "Test cry"

    def move(self):
        return "Test move"

    def sleep(self):
        return "Test sleep"

@pytest.fixture
def sample_animal():
    return MockAnimal(
        name="Sample",
        species="SampleSpecies",
        animal_group="SampleGroup",
        age=5,
        dietary_requirement="SampleFood",
        enclosure="SampleEnclosure",
        cry="SampleCry"
    )

def test_unique_id(sample_animal):
    id1 = sample_animal.get_animal_id()
    id2 = MockAnimal("A", "B", "C", 1, "D", "E","AnotherCry").get_animal_id()
    assert id1 != id2

def test_getters(sample_animal):
    assert sample_animal.get_name() == "Sample"
    assert sample_animal.get_species() == "SampleSpecies"
    assert sample_animal.get_enclosure() == "SampleEnclosure"

def test_enclosure_status_initial(sample_animal):
    assert sample_animal._Animal__enclosure_status == 3

def test_eat(sample_animal):
    sample_animal.eat()
    assert sample_animal.get_enclosure_status() == 2

def test_str_output(sample_animal):
    output = str(sample_animal)
    assert "Sample" in output
    assert "SampleEnclosure" in output

def test_clean_enclosure(sample_animal):
    sample_animal.eat()
    assert sample_animal.get_enclosure_status() == 2
    sample_animal.clean_enclosure()
    assert sample_animal.get_enclosure_status() == 3

def test_add_health_record_and_latest(sample_animal):
    sample_animal.add_health_record("01-DEC-2025", "Healthy", "Routine check-up")
    sample_animal.add_health_record("15-JUN-2025", "Injured", "Minor paw cut treated")
    latest = sample_animal.latest_health_record_str()
    assert "Status: Injured" in latest
    assert "15-JUN-2025" in latest
    assert "Minor paw cut" in latest

def test_get_health_history(sample_animal):
    sample_animal.add_health_record("07-MAY-2025", "Healthy", "Routine check-up")
    history = sample_animal.get_health_history_str()
    assert len(history) == 1
    assert "Status: Healthy" in history[0]

def test_str_output_with_health(sample_animal):
    sample_animal.add_health_record("15-JUN-2025", "Injured", "Minor paw cut treated")
    output = str(sample_animal)
    assert "Status: Injured" in output
    assert "15-JUN-2025" in output

def test_add_animal(sample_animal):
    # Reset registry to as this is a standalone test
    Animal._register = []

    # Create two animals
    a1 = MockAnimal("George", "Lion", "african savannah", 5, "meat", "Savannah", "Roar")
    a2 = MockAnimal("Simba", "Lion", "african savannah", 4, "meat", "Savannah", "Roar")

    # Registry should contain both animals
    assert a1 in Animal.get_all_animals()
    assert a2 in Animal.get_all_animals()

    # animal should not duplicate
    Animal.add_animal(a1)
    count = Animal.get_all_animals().count(a1)
    assert count == 1  # still only one instance

    # Remove one animal
    Animal.remove_animal(a1)
    assert a1 not in Animal.get_all_animals()
    assert a2 in Animal.get_all_animals()
