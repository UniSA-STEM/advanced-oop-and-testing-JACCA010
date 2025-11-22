'''
File: zoo_test.py
Description: Test file for zoo_test.
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''


import pytest
from zoo import Zoo
from JACCA010_PYTHON_UPLOAD.Animal.animal import Animal

# Mock child class for testing purposes only (reusing mock child class from previous test)
class MockAnimal(Animal):
    def cry(self): return "Test cry"
    def move(self): return "Test move"
    def sleep(self): return "Test sleep"

@pytest.fixture
def setup_zoo():
    zoo = Zoo("Cats Zoo")
    animal1 = MockAnimal("Leo", "Lion", "African Savannah", 4, "Meat", "Savannah", "Roar")
    animal2 = MockAnimal("Polly", "Parrot", "Avian", 2, "Seeds", "Aviary", "Squawk")
    return zoo, animal1, animal2

def test_add_animal(setup_zoo):
    zoo, animal1, _ = setup_zoo
    zoo.add_animal(animal1)
    assert animal1 in zoo.animals

def test_add_non_animal(setup_zoo):
    zoo, _, _ = setup_zoo
    zoo.add_animal("NotAnAnimal")
    assert len(zoo.animals) == 0

def test_remove_animal_by_id(setup_zoo):
    zoo, animal1, animal2 = setup_zoo
    zoo.add_animal(animal1)
    zoo.add_animal(animal2)
    zoo.remove_animal_by_id(animal1.get_animal_id())
    assert animal1 not in zoo.animals
    assert animal2 in zoo.animals

def test_remove_invalid_id(setup_zoo):
    zoo, animal1, _ = setup_zoo
    zoo.add_animal(animal1)
    zoo.remove_animal_by_id(999)    # ID that has not been setup
    assert animal1 in zoo.animals

def test_list_animals_output(setup_zoo):
    zoo, animal1, animal2 = setup_zoo
    zoo.add_animal(animal1)
    zoo.add_animal(animal2)
    expected = (
        f"Animals in Cats Zoo:\n"
        f"\n- [ID {animal1.get_animal_id()}]\n"
        f"  Name: Leo\n"
        f"  Species: Lion\n"
        f"  Animal Group: African Savannah\n"
        f"\n- [ID {animal2.get_animal_id()}]\n"
        f"  Name: Polly\n"
        f"  Species: Parrot\n"
        f"  Animal Group: Avian"
    )
    assert str(zoo) == expected
    print(str(zoo))


