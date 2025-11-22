'''
File: bird_test.py
Description: Test file for bird_test.
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from bird import Bird

def test_parrot_cry():
    bird = Bird("Polly", "parrot", "avian", 3, "seeds", "tropical", None)
    assert bird.cry() == "Polly Squawks!"

def test_duck_movement():
    bird = Bird("Daisy", "duck", "avian", 2, "plants", "pond", None)
    assert bird.move() == "Daisy is flying!"

def test_owl_sleep():
    bird = Bird("Hootie", "owl", "avian", 4, "mice", "forest", None)
    assert bird.sleep() == "Hootie has perched for the day."

def test_default_cry():
    bird = Bird("Chirpy", None, "avian", 1, "fruit", "aviary", None)
    assert bird.cry() == "Chirpy Chirrups!"

def test_penguin_move():
    bird = Bird("Mr Waddles", "penguin", "avian", 1, "fish", "antartic", None)
    assert bird.move() == "Mr Waddles is a flightless bird."

def test_parrot_move():
    bird = Bird("Sunshine", "parrot", "avian", 5, "seeds", "aviary", None)
    assert bird.move() == "Sunshine is flying!"

def test_default_move():
    bird = Bird("Spicy", None, "avian", 5, "seeds", "aviary", None)
    assert bird.move() == "Spicy is flying!"


