'''
File: african_savannah_test.py
Description: Special African Savannah test file to incorporate dictionary
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from african_savannah import African_Savannah

@pytest.fixture
def animals():
    lion = African_Savannah("Simba", "lion", "mammal", 5, "carnivore", "Savannah 1", "Roar")
    elephant = African_Savannah("Dumbo", "elephant", "mammal", 10, "herbivore", "Savannah 2", "Trumpet")
    gazelle = African_Savannah("Grace", "gazelle", "mammal", 3, "herbivore", "Savannah 3", "Vocalise")
    return lion, elephant, gazelle

def test_valid_species_instantiation(animals):
    lion, elephant, _ = animals
    assert lion.get_species() == "lion"
    assert elephant.get_species() == "elephant"

def test_invalid_species_raises_error():
    with pytest.raises(ValueError):
        African_Savannah("Tony", "tiger", "mammal", 4, "carnivore", "Savannah X", "Roar")

def test_cry_behavior(animals):
    lion, elephant, gazelle = animals
    assert lion.cry() == "Simba Roars!"
    assert elephant.cry() == "Dumbo Trumpets!"
    assert gazelle.cry() == "Grace Vocalises!"

def test_move_behavior(animals):
    lion, elephant, gazelle = animals
    assert lion.move() == "Simba is stalking!"
    assert gazelle.move() == "Grace is leaping!"
    assert elephant.move() == "Dumbo is swaying!"

def test_str_method(animals):
    lion, _, _ = animals
    expected = "Simba the lion lives in enclosure Savannah 1 and cries 'Roar'."
    assert str(lion) == expected

