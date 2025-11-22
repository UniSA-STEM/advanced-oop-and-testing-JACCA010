'''
File: main.py
Description: Main test file for Zoo Management System
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

from administration_staff import Administration
from african_savannah import African_Savannah
from animal import Animal
from bird import Bird
from enclosure import Enclosure
from maintenance_staff import Maintenance
from reptile import Reptile
from staff import Staff
from veterinarian_staff import Veterinarian
from zoo import Zoo
from zoo_keeper_staff import Zoo_keeper

def run_tests():
    # create zoo
    new_zoo = Zoo("Cats Menagerie")

    # add animals
    zebra = African_Savannah("Stripez", "zebra", "african savannah", "5", "assorted grasses", "savannah", "Vocalise")
    owl = Bird("Hoobert", "Owl","bird", "2", "mice", "aviary", "Hoot")
    crocodile = Reptile("Chomper", "crocodile", "reptile", "25", "meat, chicken, fish","pond", "Growl")

    new_zoo.add_animal(zebra)
    new_zoo.add_animal(owl)
    new_zoo.add_animal(crocodile)

    # list animals
    new_zoo.list_animals()

    # create staff
    admin = Administration("Jonathon", "Livingston")
    vet = Veterinarian ("Dianna", "Dolittle")
    keeper = Zoo_keeper("Jane", "Goodall")
    maintenance = Maintenance("Bob", "Fixit")

    print(admin)
    print(vet)
    print(keeper)
    print(maintenance)

    # create enclosure and add animals
    savannah = Enclosure("Savannah", "Small")
    savannah.add_animal(zebra)
    print(savannah)


if __name__ == "__main__":
    run_tests()
