'''
File: zoo_keeper_staff.py
Description: Child class (zoo keeper) of parent (staff) class
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

from JACCA010_PYTHON_UPLOAD.Staff.staff import Staff

class Zoo_keeper(Staff):

    def __init__(self, first_name, surname):
        super().__init__(first_name,surname, "Zoo Keeper")

    def __str__(self):
        return (
            f"ID: {self.staff_id}\n"
            f"Name: {self.first_name} {self.surname}\n"
            f"Occupation: {self.get_occupation()}"
        )