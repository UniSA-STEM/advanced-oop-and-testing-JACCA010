'''
File: bird.py
Description: Bird class as child class of animal class for zoo management system.
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''


# Parent Class will require removal of duplicate code in child class
from animal import Animal

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

    # method for eating which will also reduce available food by 1 unit and require refill at 0 units
    # to increase enclosure mess by 1 unit (num units for cleaning enclosure to be max 3)
    # max food units to be set at three

    def bird_eat(self):
        bird_eat = 0

        while bird_eat < Animal.max_food():
            bird_eat +=1

        if bird_eat == Animal.max_food():
            print (f"{self.__name} has eaten all the food.")
            print (f"Please refill food.")

        else:
            print (f"Yummy!")



