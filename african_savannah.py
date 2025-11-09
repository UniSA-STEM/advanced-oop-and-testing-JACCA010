'''
File: african_savannah.py
Description: Special African Savannah class as child class of animal class for zoo management system.
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class African_Savannah(Animal):
    # species list can be updated as additional african savannah animals are added to the zoo
    african_species_dict = [
        "lion"
        "elephant"
        "giraffe"
        "zebra"
        "cheetah"
        "hyena"
        "wildebeest"
        "gazelle"
        "antelope"
        "aardvark"
    ]
    def __init__(self, name, species, animal_group, age, dietary_requirement,enclosure, cry):
        super().__init__(name, species, animal_group, age, dietary_requirement, enclosure, cry)
        self.__african_species = species

    def cry(self):    # to be made species dependant where relevant and allow for edits as new animals added
        if self.get_species() == "lion":
            sound = "Roar"
        elif self.get_species() == "elephant":
            sound = "Trumpet"
        elif self.get_species() == "zebra":
            sound = "Bray"
        elif self.get_species() == "hyena":
            sound = "Laugh"
        else:
            sound = "Vocalise"
        print (f"{self.get_name()} {sound}s!")

    def move(self):    # simple movements based on species type
        if self.get_species() == "lion":
            print (f"{self.get_name()} is stalking.")
        elif self.get_species() == "gazelle" or self.get_species() == "antelope":
            print (f"{self.get_name()} is leaping.")
        else:
            print (f"{self.get_name()} is walking.")

    def sleep(self):
        print (f"{self.get_name()} is sleeping.")

