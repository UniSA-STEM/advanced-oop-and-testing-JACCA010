'''
File: reptile.py
Description: Reptile class as child class of animal class for zoo management system.
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''


# Parent Class will require removal of duplicate code in child class
from animal import Animal

class Reptile:
    def __init__(self, name, species, animal_group, age, dietary_requirement,enclosure, cry):
        self.__name = name
        self.__species = species
        self.__animal_group = animal_group("Reptile")
        self.__age = age
        self.__dietary_requirement = dietary_requirement # to be defined based on species
        self.__enclosure = enclosure("Reptile Tank")
        self.__cry = cry # to be defined based on species

    # Reptile child class with predefined attributes

    # method for eating which will also reduce available food by 1 unit and require refill at 0 units
    # to increase enclosure mess by 1 unit (num units for cleaning enclosure to be max 3)
    # max food units to be set at three

    def reptile_eat(self):
        reptile_eat = 0

        while reptile_eat < Animal.max_food():
            reptile_eat +=1

        if reptile_eat == Animal.max_food():
            print (f"{self.__name} has eaten all the food.")
            print (f"Please prepare more food.")

        else:
            print (f"Yummy!")

    # dietary requirement for reptiles will be Mice for Snakes and Worms and Bugs for all other reptiles

    def dietary_requirement(self):
        if self.__species == "Snake":
            self.__dietary_requirement = "Mice"

        else:
            self.__dietary_requirement = "Bugs and Worms"

        return self.__dietary_requirement

    def cry(self):
        if self.__species == "Snake":
            self.__cry = "Hiss"

        else:
            self.__cry = "Chitter"

        return self.__cry