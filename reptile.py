'''
File: reptile.py
Description: Reptile class as child class of animal class for zoo management system.
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Reptile(Animal):
    def __init__(self, name, species, animal_group, age, dietary_requirement,enclosure, cry):
        super().__init__(name, species, animal_group, age, dietary_requirement, enclosure, cry)

    def cry(self):    # to be made species dependant and allow for edits as new animals added
        if self.get_species() == "snake":
            sound = "Hiss"
        elif self.get_species() == "lizard":
            sound = "Click"
        elif self.get_species() == "crocodile" or self.get_species == "alligator":
            sound = "Growl"
        elif self.get_species() == "frog" or self.get_species == "toad":    # although amphibian have included in this class for test purposes
            sound = "Ribbet"
        else:
            sound = "Puff"
        print (f"{self.get_name()} {sound}s!")

    def move(self):    # simple movements based on species type
        if self.get_species() == "snake":
            print (f"{self.get_name()} is slithering.")
        elif self.get_species() == "crocodile":
            print (f"{self.get_name()} is stalking.")
        else:
            print (f"{self.get_name()} is walking.")

    def sleep(self):    # simple sleep based on species type
        if self.get_species() == "snake":
            print (f"{self.get_name()} has coiled up and is sleeping.")
        else:
            print (f"{self.get_name()} is sleeping.")

    def sunning(self):    # reptiles like to rest in the sun
        if self.get_species() == "snake" or self.get_species == "lizard":
            print (f"{self.get_name()} is resting on a sunny rock.")
        else:
            print (f"{self.get_name()} is warming itself in the sun.")