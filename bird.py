'''
File: bird.py
Description: Bird class as child class of animal class for zoo management system.
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal  # Parent Class will require removal of duplicate code in child class

class Bird:
    def __init__(self, name, species, animal_group, age, dietary_requirement,enclosure, cry):
        self.__name = name
        self.__species = species
        self.__animal_group = animal_group("Avian")
        self.__age = age
        self.__dietary_requirement = dietary_requirement("Seeds and Fruit")
        self.__enclosure = enclosure("Aviary")
        self.__cry = cry("Squawk")

    # Bird child class with predefined attributes noting this does not include birds of prey

