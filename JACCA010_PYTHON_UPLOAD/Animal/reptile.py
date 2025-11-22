'''
File: reptile.py
Description: Reptile class as child class of animal class for zoo management system.
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

from JACCA010_PYTHON_UPLOAD.Animal.animal import Animal

class Reptile(Animal):
    def __init__(self, name, species, animal_group, age, dietary_requirement,enclosure, cry):
        super().__init__(name, species, animal_group, age, dietary_requirement, enclosure, cry)

    def __str__(self):    # adding string method
        return f"{self.get_name()} the {self.get_species()} lives in enclosure {self.get_enclosure()} and cries '{self.cry()}'."

    def cry(self):    # to be made species dependant and allow for edits as new animals added
        species = self.get_species()
        if species is None:
            return None
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
        reptile_sound = (f"{self.get_name()} {sound}s!")
        print (reptile_sound)
        return reptile_sound

    def move(self):    # simple movements based on species type
        if self.get_species() == "snake":
            reptile_move = (f"{self.get_name()} is slithering.")
        elif self.get_species() == "crocodile":
            reptile_move = (f"{self.get_name()} is stalking.")
        else:
            reptile_move = (f"{self.get_name()} is walking.")
        print (reptile_move)
        return reptile_move

    def sleep(self):    # simple sleep based on species type
        if self.get_species() == "snake":
            reptile_sleep = (f"{self.get_name()} has coiled up and is sleeping.")
        else:
            reptile_sleep = (f"{self.get_name()} is sleeping.")
        print (reptile_sleep)
        return reptile_sleep

    def sunning(self):    # reptiles like to rest in the sun
        if self.get_species() == "snake" or self.get_species == "lizard":
            sunning = (f"{self.get_name()} is resting on a sunny rock.")
        else:
            sunning = (f"{self.get_name()} is warming itself in the sun.")
        print (sunning)
        return sunning