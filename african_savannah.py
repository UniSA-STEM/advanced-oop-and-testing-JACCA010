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
    # species dictionary can be updated as additional african savannah animals are added to the zoo

    african_species_dict = {
        "lion": {"cry": "Roar", "move": "stalking"},
        "elephant": {"cry": "Trumpet", "move": "swaying"},
        "giraffe": {"cry": "Vocalise", "move": "walking"},
        "zebra": {"cry": "Vocalise", "move": "walking"},
        "cheetah": {"cry": "Vocalise", "move": "stalking"},
        "hyena": {"cry": "Laugh", "move": "walking"},
        "wildebeest": {"cry": "Vocalise", "move": "walking"},
        "gazelle": {"cry": "Vocalise", "move": "leaping"},
        "antelope": {"cry": "Vocalise", "move": "leaping"},
        "aardvark": {"cry": "Vocalise", "move": "walking"}
    }
    def __init__(self, name, species, animal_group, age, dietary_requirement,enclosure, cry):
        # error validation checking
        if species not in self.african_species_dict:
            raise ValueError(f"{species} is not recognized as an African savannah species.")
        super().__init__(name, species, animal_group, age, dietary_requirement, enclosure, cry)
        self.__african_species = species

    def __str__(self):    # adding string method
        return f"{self.get_name()} the {self.get_species()} lives in enclosure {self.get_enclosure()} and cries '{self._Animal__cry}'."

    def cry(self):
        sound = self.african_species_dict.get(self.get_species(), {}).get("cry", "Vocalise")
        return (f"{self.get_name()} {sound}s!")

    def move(self):    # simple movements based on species type
        action = self.african_species_dict.get(self.get_species(), {}).get("move", "walking")
        return (f"{self.get_name()} is {action}!")

    def sleep(self):    # simple implementation of sleep
        print (f"{self.get_name()} is sleeping.")