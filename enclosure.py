'''
File: enclosure.py
Description: Enclosure class to manage animal enclosure attributes
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''


class Enclosure:
    _id_counter = 1  # adding unique ID identifier

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
            "Bespoke": {"animal_groups": None, "max_animals": 1}
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
                self.__animal_group if isinstance(self.__animal_group, list)
                else [self.__animal_group] if self.__animal_group
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

    # method to summarise the species in the enclosures
    def summary(self):
        species_counts = {}
        for animal in self.__animals:
            species = animal.get_species()
            species_counts[species] = species_counts.get(species, 0) + 1
        return species_counts

    # method to upgrade enclosure once full (if applicable)
    def upgrade_enclosure(self):
        if self.enclosure_capacity() == "Full" and self.__size != "Large":
            if self.__size == "Small":
                return self._apply_size_change("Medium")
            elif self.__size == "Medium":
                return self._apply_size_change("Large")
        elif self.__size == "Large" or self.enclosure_capacity() != "Full":
            print (f"Upgrade not required for enclosure '{self.__enclosure_type}'")
            return self.__size

    # method to downgrade enclosure when number of animals in the species reduce
    # using "species count" class method from Animal class
    def downgrade_enclosure(self):
        if self.__size == "Small":
            print (f"Enclosure '{self.__enclosure_type}' is already at minimum size")
            return self.__size
        # use count species method
        species_counts = self.summary()
        total_animals = sum(species_counts.values())
        if total_animals <= 10:
            return self._apply_size_change("Small")
        elif total_animals <= 30:
            return self._apply_size_change("Medium")
        else:
            print(f"Downgrade not required for enclosure '{self.__enclosure_type}'")
            return self.__size

    # apply size change method to simplify upgrade and downgrade methods
    # including validation of size (will also allow new enclosure sizes to be added at a later date)
    def _apply_size_change(self, new_size: str) -> str:
        type_data = Enclosure.enclosure_type_dict.get(self.__enclosure_type)
        if not type_data or new_size not in type_data:
            print(f"Invalid size '{new_size}' for enclosure '{self.__enclosure_type}'")
            return self.__size
        self.__size = new_size
        self.__animal_group = type_data[new_size]["animal_groups"]
        self.__max_animals = type_data[new_size]["max_animals"]
        print(f"Enclosure '{self.__enclosure_type}' set to '{new_size}' "
              f"with capacity {self.__max_animals}.")
        return self.__size


    # add move animals to allow transfer between enclosures



    # add rule to ensure one species only per enclosure

    def check_enclosure_species(self, animal):
        if not self.__animals:
            return True
        return all(existing.species == animal.species for existing in self.__animals)

    def __str__(self):
        return(
            f"Enclosure Type: {self.__enclosure_type}\n"
            f"Size: {self.__size}\n"
            f"Animal Group: {self.__animal_group}\n"
            f"Maximum Animals: {self.__max_animals}\n"
            f"Current Capacity: {self.enclosure_capacity()}"
       )

    # enclosure ID initiated as a property

    @property
    def enclosure_id(self):
        return self.__enclosure_id
