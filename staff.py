'''
File: staff.py
Description: Staff file to manage zoo personnel.
Author: Catherine Jackson
ID: 110481962
Username: jacca010
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Staff:
    _id_counter = 1
    _register = []    # register of staff

    def __init__(self, staff_id, first_name, surname, occupation):
        self.__staff_id = Staff._id_counter
        Staff._id_counter += 1
        self.__first_name = first_name
        self.__surname = surname
        self.__occupation = occupation

        # global registry of staff
        Staff._register.append(self)

    # adding class method for count_staff (for personnel management)
    @classmethod
    def count_staff(cls, staff_id):
        return sum(1 for staff_id in cls._register if staff.get__id == staff_id)

    # adding class method to add and remove staff and return list of all staff
    @classmethod
    def add_staff(cls, staff):
        if staff not in cls._register:
            cls._register.append(staff)

    @classmethod
    def remove_staff(cls, staff):
        if staff in cls._register:
            cls._register.remove(staff)

    @classmethod
    def get_all_staff(cls):
       return list(cls._register)

    # Getters
    def get_staff_id(self):
        return self.__staff_id

    def get_first_name(self):
        return self.__first_name

    def get_surname(self):
        return self.__surname

    def get_occupation(self):
        return self.__occupation

    # properties added to staff

    @property
    def staff_id(self):
        return self.__staff_id

    def first_name(self):
        return self.__first_name

    def surname(self):
        return self.__surname

    def __str__(self):
        return (
            f"ID: {self.__staff.id}\n"
            f"Name: {self.__first_name} {self.__surname}\n"
            f"Occupation: {self.__occupation}"
        )
