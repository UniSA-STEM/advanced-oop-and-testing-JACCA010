'''
File: animal.py
Description: Animal class code for zoo management system
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:
    def __init__(self, name, species, animal_group, age, dietary_requirement, enclosure, cry):
        self.__name = name
        self.__species = species
        self.__animal_group = animal_group
        self.__age = age
        self.__dietary_requirement = dietary_requirement
        self.__enclosure = enclosure
        self.__cry = cry

    # animal class includes attributes applicable to all animals regardless of species.
    # purpose is to capture attributes which are going to be consistently used and will

    def create_animal(self):  # create new animal
        pass

    # create setters and getters within animal class

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_species(self, species):
        self.__species = species

    def get_species(self):
        return self.__species

    def set_animal_group(self, animal_group):
        self.__animal_group = animal_group

    def get_animal_group(self):
        return self.__animal_group

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_dietary_requirement(self, dietary_requirement):
        self.__dietary_requirement = dietary_requirement

    def get_dietary_requirement(self):
        return self.__dietary_requirement

    def set_enclosure(self, enclosure):
        self.__enclosure = enclosure

    def get_enclosure(self):
        return self.__enclosure

    def set_cry(self, cry):
        self.__cry = cry

    def get_cry(self):
        return self.__cry




