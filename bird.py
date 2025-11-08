'''
File: bird.py
Description: Bird class as child class of animal class for zoo management system.
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Bird(Animal):
    def __init__(self, name, species, animal_group, age, dietary_requirement,enclosure, cry):
        super().__init__(name, species, animal_group, age, dietary_requirement, enclosure, cry)

    @property
    def cry(self):    # to be made species dependant and allow for edits as new animals added
        if self.species == "parrot":
            return "Squawk"
        elif self.species == "duck":
            return "Quack"
        elif self.species == "owl":
            return "Hoot"
        elif self.species == None:
            return "Chirrup"
        print (f"{self.cry}!")

    @property
    def move(self):
        print (f"{self.name} is flapping its wings!")    # valid also for non-flight birds

    @property
    def sleep(self):
        if self.species !- "owl":    # given owls hunt at night and sleep during the day have created day/night sleep.
            print (f"{self.name} has perched for the night.")
        else:
            print (f"{self.name} has perched for the day.")

        # future iteration of zoo management system could include nocturnal animals as a separate class
