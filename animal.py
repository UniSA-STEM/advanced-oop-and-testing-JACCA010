'''
File: animal.py
Description: Animal class code for zoo management system
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod    # adding abstract method into parent class

class Animal(ABC):
    _id_counter = 1    # adding unique ID identifier

    def __init__(self, name, species, animal_group, age, dietary_requirement, enclosure, cry):
        self.__animal_id = Animal._id_counter
        Animal._id_counter += 1

        self.__name = name
        self.__species = species
        self.__animal_group = animal_group
        self.__age = age
        self.__dietary_requirement = dietary_requirement
        self.__enclosure = enclosure
        self.__cry = cry
        self.__enclosure_status = 3    # initialise at maximum cleanliness

    # animal class includes attributes applicable to all animals regardless of species.
    # purpose is to capture attributes which are going to be consistently used and will

    # Unique ID
    def get_animal_id(self):    # animal unique identifier
        return self.__animal_id

    # Animal Name
    def set_name(self, name):    # each animal will have a name eg spot, spike, George etc
        self.__name = name

    def get_name(self):
        return self.__name

    # species
    def set_species(self, species):    # each animal will be part of a species eg parrot and owl are avian species, snake and lizard are reptile species
        self.__species = species

    def get_species(self):
        return self.__species

    # group (eg Avian, reptile etc_
    def set_animal_group(self, animal_group):    # eg avian, aquatic, reptile, big cat etc
        self.__animal_group = animal_group

    def get_animal_group(self):
        return self.__animal_group

    # age (NB there is no max age)
    def set_age(self, age):    # at entry each animal will have an age
        self.__age = age

    def get_age(self):
        return self.__age

    # dietary requirement
    def set_dietary_requirement(self, dietary_requirement):    # each animal will have a dietary requirement eg seeds and fruit, mice and rats, meat etc
        self.__dietary_requirement = dietary_requirement

    def get_dietary_requirement(self):
        return self.__dietary_requirement

    # enclosure type
    def set_enclosure(self, enclosure):    # each animal will have an enclosure type
        self.__enclosure = enclosure

    def get_enclosure(self):
        return self.__enclosure

    # cry

    def set_cry(self, cry):
        self._cry = cry

    def get_cry(self):
        return self._cry

    # enclosure status
    def get_enclosure_status(self):
        return self._enclosure_status

    # will be consistent method across all animals.  Holding in parent class avoids duplication of code.
    # method for eating which will also reduce available food by 1 unit and require refill at 0 units
    # to increase enclosure mess by 1 unit (num units for cleaning enclosure to be max 3)
    # max food for all animals has been set to three before refill and enclosure clean will be initiated

    def eat(self):
        eat = 0
        enclosure_status = 3    # to allow for status reduction as eat increases

        while eat < self.max_food():
            eat += 1
            enclosure_status -= 1

        if eat == self.max_food():
            print(f"{self.__name} has eaten all the food.")
            print(f"Please refill food.")

        else:
            print(f"Yummy!")

        if self._enclosure_status == 0:
            print (f"{self.__name}'s {self.__enclosure} is messy. Please clean before next feed.")

    @abstractmethod
    def cry(self):
        pass    # to be defined in child class

    @abstractmethod
    def move(self):
        pass    # to be defined in child class

    @abstractmethod
    def sleep(self):    # to be defined in child class
        pass

    @property    # amended max food to property
    def max_food(self):
        return 3

    def __str__(self):    # string representation
        return f"[ID {self.__animal_id}] {self.__name} the {self.__species} ({self.__animal_group}) in {self.__enclosure}"

