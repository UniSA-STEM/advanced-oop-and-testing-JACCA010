'''
File: main.py
Description: Main test file for Zoo Management System
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

from JACCA010_PYTHON_UPLOAD.Staff.administration_staff import Administration
from JACCA010_PYTHON_UPLOAD.Animal.african_savannah import African_Savannah
from JACCA010_PYTHON_UPLOAD.Animal.animal import Animal
from JACCA010_PYTHON_UPLOAD.Animal.bird import Bird
from JACCA010_PYTHON_UPLOAD.Enclosure.enclosure import Enclosure
from JACCA010_PYTHON_UPLOAD.Staff.maintenance_staff import Maintenance
from JACCA010_PYTHON_UPLOAD.Animal.reptile import Reptile
from JACCA010_PYTHON_UPLOAD.Staff.staff import Staff
from JACCA010_PYTHON_UPLOAD.Staff.veterinarian_staff import Veterinarian
from JACCA010_PYTHON_UPLOAD.Enclosure.zoo import Zoo
from JACCA010_PYTHON_UPLOAD.Staff.zoo_keeper_staff import Zoo_keeper

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

    # boutique tests for animal class testing (drawn from unittest cases)

    # Mock child class for testing purposes only
    class MockAnimal(Animal):
        def cry(self): return "Test cry"
        def move(self): return "Test move"
        def sleep(self): return "Test sleep"

    # Unique ID test
    a1 = MockAnimal("Sample", "SpeciesA", "GroupA", 5, "FoodA", "EnclosureA", "CryA")
    a2 = MockAnimal("Another", "SpeciesB", "GroupB", 3, "FoodB", "EnclosureB", "CryB")
    print("[Unique ID Test]")
    print("ID1:", a1.get_animal_id(), "ID2:", a2.get_animal_id())
    assert a1.get_animal_id() != a2.get_animal_id()

    # Getter test
    print("[Getter Test]")
    print("Name:", a1.get_name(), "Species:", a1.get_species(), "Enclosure:", a1.get_enclosure())
    assert a1.get_name() == "Sample"
    assert a1.get_species() == "SpeciesA"
    assert a1.get_enclosure() == "EnclosureA"

    # Enclosure status test
    print("[Enclosure Status Test]")
    print("Initial status:", a1.get_enclosure_status())
    a1.eat()
    print("After eating:", a1.get_enclosure_status())
    assert a1.get_enclosure_status() == 2

    # Clean enclosure test
    print("[Clean Enclosure Test]")
    a1.clean_enclosure()
    print("After cleaning:", a1.get_enclosure_status())
    assert a1.get_enclosure_status() == 3

    # Health record test (dict version)
    print("\n[Health Record Test - Dict]")
    a1.add_health_record("01-DEC-2025", "Healthy", "Routine check-up")
    a1.add_health_record("15-JUN-2025", "Injured", "Minor hoof injury treated")
    latest = a1.latest_health_record_dict()
    print("Latest record (dict):", latest)
    assert latest["Status"] == "Injured"
    assert "Minor hoof injury treated" in latest["Notes"]

    # Health record test (string version)
    print("\n[Health Record Test - String]")
    print("Latest record (string):", a1.latest_health_record_str())
    print("Full history (string):")
    for record in a1.get_health_history_str():
        print("-", record)

    # Health record test with real animal
    print("\n[Health Record Test with Animal]")
    zebra = African_Savannah("Stripez", "zebra", "African Savannah", 4,
                             "assorted grasses", "Savannah", "Vocalise")
    zebra.add_health_record("15-JUN-2025", "Injured", "Minor hoof injury treated")
    zebra.add_health_record("01-DEC-2025", "Healthy", "Routine check-up")
    print("Latest zebra record:", zebra.latest_health_record_str())
    print("Zebra history:")
    for record in zebra.get_health_history_str():
        print("-", record)

    # Registry test
    print("[Registry Test]")
    print("Registry:")
    for animal in Animal.get_all_animals():
        print("-", animal.get_name(), "|", animal.get_species(), "|", animal.get_enclosure())

    print("\n=== All boutique tests completed successfully ===")

if __name__ == "__main__":
    run_tests()
