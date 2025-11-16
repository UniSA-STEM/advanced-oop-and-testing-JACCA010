'''
File: enclosure.py
Description: Enclosure class to manage animal enclosure attributes
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''


class Enclosure:

    # enclosure dictionary
    enclosure_type_dict = {
        "Aviary": {
            "Small": {"animal_groups": ["bird"], "max_animals": 10},
            "Medium": {"animal_groups": ["bird"], "max_animals": 30},
            "Large": {"animal_groups": ["bird"], "max_animals": 50}
        },
        "Pond": {
            "Small": {"animal_groups": ["reptile", "amphibian", "bird"], "max_animals": 10},
            "Medium": {"animal_groups": ["reptile", "amphibian", "bird"], "max_animals": 30},
            "Large": {"animal_groups": ["reptile", "amphibian", "bird"], "max_animals": 30},
        },
        "Savannah": {
            "Small": {"animal_groups": ["african savannah"], "max_animals": 10},
            "Medium": {"animal_groups": ["african savannah"], "max_animals": 30},
            "Large": {"animal_groups": ["african savannah"], "max_animals": 50},
        },
        "Antarctic": {
            "Small": {"animal_groups": ["bird"], "max_animals": 10},
            "Medium": {"animal_groups": ["bird"], "max_animals": 30},
            "Large": {"animal_groups": ["bird"], "max_animals": 50},
        },
        "Quarantine":  {
            "Bespoke": {"animal_groups": None, "max_animals": 1
        }}



    def __init__(self, enclosure_type, size, animal_group=None, max_animals=0):
        self.__enclosure_id = Enclosure._id_counter    # enclosure ID added
        Enclosure._id_counter += 1


        self.__enclosure_type = enclosure_type
        self.__size = size
        self.__animal_group = animal_group
        self.__max_animals = max_animals
        self.__animals = []    # to hold Animal instances within the enclosure

    # method to allow new enclosure_types to be added
    def add_enclosure_type(self, new_type=None, new_size=None, base_type=None, base_size=None):

        # duplicating an enclosure

        if base_type and base_size:
            if base_type in Enclosure.enclosure_type_dict and base_size in Enclosure.enclosure_type_dict[base_type]:
                source = Enclosure.enclosure_type_dict[base_type][base_size]
                new_enclosure = {
                    "animal_groups": source["animal_groups"],
                    "max_animals": source["max_animals"],
                }
            else:
                raise ValueError(f"Cannot duplicate: '{base_type}' with size '{base_size}' not found.")

        # adding a new enclosure type (not already in list)
        else:
            group_list = (
                self.animal_group if isinstance(self.animal_group, list)
                else [self.animal_group] if self.animal_group
                else []
            )
            new_enclosure = {
                "animal_groups": group_list,
                "max_animals": self.__max_animals
            }

        # Add the new enclosure to the dictionary
        if new_type not in Enclosure.enclosure_type_dict:
            Enclosure.enclosure_type_dict[new_type] = {}
        Enclosure.enclosure_type_dict[new_type][new_size] = new_enclosure

    # method to add animals into the enclosures
    def add_animal(self, animal):
        if len(self.__animals) < self.__max_animals:
            self.__animals.append(animal)
        else:
            print(f"Enclosure '{self.__enclosure_type}' ({self.__size}) is at full capacity.")

    # method to calculate current capacity of enclosure (ie 25%, 50%)
    def enclosure_capacity(self):
        if self.__max_animals == 0:
            return "Undefined"
        percent = (len(self.__animals) / self.__max_animals) * 100
        if percent == 0:
            return "Empty"
        elif percent < 25:
            return "Low (under 25%)"
        elif percent < 50:
            return "Moderate (under 50%)"
        elif percent < 75:
            return "High (under 75%)"
        elif percent < 100:
            return "Near Full (under 100%)"
        else:
            return "Full"

    def __str__(self):
        return(
            f"Enclosure Type: {self.__enclosure_type}\n"
            f"Size: {self.__size}\n"
            f"Animal Group: {self.animal_group}\n"
            f"Maximum Animals: {self.__max_animals}\n"
            f"Current Capacity: {self.enclosure_capacity()}"
        )