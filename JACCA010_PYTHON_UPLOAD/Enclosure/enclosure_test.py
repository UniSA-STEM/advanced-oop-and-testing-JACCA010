'''
File: enclosure_test.py
Description: Test file for enclosure_tests
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from JACCA010_PYTHON_UPLOAD.Enclosure.enclosure import Enclosure
from JACCA010_PYTHON_UPLOAD.Animal.animal import Animal

# Mock child class for testing purposes only

class MockAnimal(Animal):
    def cry(self):
        return "Test cry"

    def move(self):
        return "Test move"

    def sleep(self):
        return "Test sleep"

@pytest.fixture
def setup_enclosures():
    pond_small = Enclosure("Pond", "Small", "amphibian", 10)
    aviary_small = Enclosure("Aviary", "Small", "bird", 10)
    savannah_medium = Enclosure("Savannah", "Medium", "african savannah", 30)
    frog = MockAnimal("Kermit", "frog", "reptile", 2, "bugs", "Pond", "Ribbet")
    owl = MockAnimal("Hoobert", "Owl", "bird", 5, "Mice", "Aviary", "Hoot")
    zebra = MockAnimal("Stripez", "Zebra", "african savannah", 3, "assorted grasses", "Savannah", "Vocalise")
    return pond_small, aviary_small, savannah_medium, frog, owl, zebra

def test_enclosure_id_unique(setup_enclosures):
    e1 = Enclosure("Aviary", "Small", "bird", 10)
    e2 = Enclosure("Pond", "Small", "amphibian", 10)
    e3 = Enclosure("Savannah", "Medium", "african savannah", 30)
    assert e1.enclosure_id != e2.enclosure_id
    assert e1.enclosure_id != e3.enclosure_id
    assert e2.enclosure_id != e3.enclosure_id

def test_add_animal_and_summary(setup_enclosures):
    _, aviary_small, _, _,  owl, _ = setup_enclosures
    aviary_small.add_animal(owl)
    summary = aviary_small.summary()
    assert summary["Owl"] == 1
    assert "frog" not in summary

def test_enclosure_capacity(setup_enclosures):
    _, aviary_small, _, _, owl, _ = setup_enclosures
    assert aviary_small.enclosure_capacity() == "Empty"
    aviary_small.add_animal(owl)
    assert aviary_small.enclosure_capacity() == "Low (under 25%)"

def test_upgrade_enclosure(setup_enclosures):
    _, aviary_small, _, _, _, _ = setup_enclosures
    for i in range(10):
        aviary_small.add_animal(MockAnimal(f"Bird{i}", "Parrot", "bird", 1, "Seeds", "Aviary", "Squawk"))
    assert aviary_small.enclosure_capacity() == "Full"
    new_size = aviary_small.upgrade_enclosure()
    assert new_size == "Medium"

def test_downgrade_enclosure(setup_enclosures):
    _, _, savannah_medium, _, _, zebra = setup_enclosures
    savannah_medium.add_animal(zebra)
    new_size = savannah_medium.downgrade_enclosure()
    assert new_size == "Small"

def test_move_animals_success(setup_enclosures):
    pond_small, aviary_small, _, _, owl, _ = setup_enclosures
    aviary_small.add_animal(owl)
    moved = aviary_small.move_animals(owl, pond_small)
    assert moved is True
    assert aviary_small.summary() == {}
    assert pond_small.summary()["Owl"] == 1


# add edge case to test maximum capacity
def test_add_animal_beyond_capacity(setup_enclosures):
    _, aviary_small, _, _, _, _ = setup_enclosures
    for i in range(10):
        aviary_small.add_animal(MockAnimal(f"Bird{i}", "Owl", "bird", 1, "Mice", "Aviary", "Hoot"))
    extra_bird = MockAnimal("Extra", "Owl", "bird", 1, "Mice", "Aviary", "Hoot")
    aviary_small.add_animal(extra_bird)
    summary = aviary_small.summary()
    total = sum(summary.values())
    assert total == 10

def test_move_animal_not_in_source(setup_enclosures):
    pond_small, aviary_small, _, _, owl, _ = setup_enclosures
    moved = aviary_small.move_animals(owl, pond_small)
    assert moved is False


