'''
File: zoo.py
Description: Zoo class created to manage various zoo features such as adding and removing animals
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

from JACCA010_PYTHON_UPLOAD.Animal.animal import Animal


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []    # to hold list of all animals in the zoo

    # add animal
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.get_name()} the {animal.get_species()} has entered {self.name}.")
        else:
            print("Only Animal instances can be added.")

    # remove animal by ID
    def remove_animal_by_id(self, animal_id):
        for a in self.animals:
            if a.get_animal_id() == animal_id:
                self.animals.remove(a)
                print(f"Animal ID {animal_id} has been removed from {self.name}.")
                return
        print(f"No animal with ID {animal_id} found in {self.name}.")

    def __contains__(self, animal_id):    # allows look up based on ID
        return any(a.get_animal_id() == animal_id for a in self.animals)

    def list_animals(self):    # returns list of animals in zoo
        print(self.__str__())

    # count of animals in enclosures (to help measure enclosure capacity)
    def count_animals(self):
        count = 0
        for animal in self.animals:
            if hasattr(animal, "enclosure") and animal.enclosure is not None:
                count += 1
        return count

    def __str__(self):
        output = [f"Animals in {self.name}:"]
        for a in self.animals:
            output.append(
                f"\n- [ID {a.get_animal_id()}]\n"
                f"  Name: {a.get_name()}\n"
                f"  Species: {a.get_species()}\n"
                f"  Animal Group: {a.get_animal_group()}"
            )
        return "\n".join(output)

