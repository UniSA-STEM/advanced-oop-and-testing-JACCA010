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

    def cry(self):    # to be made species dependant and allow for edits as new animals added
        if self.get_species() == "parrot":
            sound = "Squawk"
        elif self.get_species() == "duck":
            sound = "Quack"
        elif self.get_species() == "owl":
            sound = "Hoot"
        else:
            sound = "Chirrup"
        print (f"{self.get_name()} {sound}s!")

    def move(self):
        print (f"{self.get_name()} is flapping its wings!")    # valid also for non-flight birds

    def sleep(self):
        if self.get_species != "owl":    # given owls hunt at night and sleep during the day have created day/night sleep.
            print (f"{self.get_name()} has perched for the night.")
        else:
            print (f"{self.get_name()} has perched for the day.")

        # future iteration of zoo management system could include nocturnal animals as a separate class

