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
    def __init__(self, name, species, animal_group, age, dietary_requirement,enclosure, cry, flight_ability=None):
        super().__init__(name, species, animal_group, age, dietary_requirement, enclosure, cry)
        self.__flight_ability = flight_ability

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
        if self.flight_ability() == "flightless":
            print (f"{self.get_name()} is a flightless bird.")
        else:
            print (f"{self.get_name()} is flying!")

    def sleep(self):
        if self.get_species != "owl":    # given owls hunt at night and sleep during the day have created day/night sleep.
            print (f"{self.get_name()} has perched for the night.")
        else:
            print (f"{self.get_name()} has perched for the day.")

        # future iteration of zoo management system could include nocturnal animals as a separate class

    def flight_ability(self):    # adding flight capability to bird class
        species = self.get_species()
        flightless_species = {"penguin", "emu", "ostrich", "cassowary", "kiwi"}
        return "flightless" if species in flightless_species else "flight capable"



