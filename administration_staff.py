'''
File: administration_staff.py
Description: Child class (administration) of parent (staff) class
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff

class Administration(Staff):

    def __init__(self, staff_id, first_name, surname, occupation="Administration"):
        super().__init__(staff_id, first_name,surname, occupation)
        self.occupation = "Administration"

    def __str__(self):
        return (
            f"ID: {self.staff_id}\n"
            f"Name: {self.first_name} {self.surname}\n"
            f"Occupation: {self.occupation}"
        )