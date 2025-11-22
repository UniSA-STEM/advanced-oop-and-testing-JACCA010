'''
File: reptile_test.py
Description: Test file for reptile_test.
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from reptile import Reptile

def test_tortoise_cry():
    reptile = Reptile("Sleepy", "tortoise", "reptile", 32, "green leaves", "pond", None)
    assert reptile.cry() == "Sleepy Puffs!"

def test_tortoise_cry_none():
    reptile = Reptile("Sleepy", None, "reptile", 32, "green leaves", "pond", None)
    assert reptile.cry() == None

def test_frog_cry():
    reptile = Reptile("Prince Toadie", "frog", "reptile", 2,"green leaves", "pond", None)
    assert reptile.cry() == "Prince Toadie Ribbets!"

def test_crocodile_movement():
    reptile = Reptile("Roger", "crocodile", "reptile", 10, "carnivore", "pond", None)
    assert reptile.move() == "Roger is stalking."

def test_snake_sleep():
    reptile = Reptile("Simon", "snake", "reptile", 4, "mice", "rock bed",None)
    assert reptile.sleep() == "Simon has coiled up and is sleeping."

