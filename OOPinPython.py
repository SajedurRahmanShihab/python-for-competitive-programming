class Person:
    def __init__(self, person_name: str, year_of_birth: int, ht_inches=None):
        self.__name = person_name
        self.__year_of_birth = year_of_birth
        self.__height_inches = ht_inches
        self.abc = None

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if(self.__has_any_number(new_name)):
            print("Sorry person name can't have number")
        self.__name = new_name

    def __has_any_number(self, string):
        return "0" in string

    def get_summary(self):
        return f"Name: {self.__name}, DOB: {self.__year_of_birth}, Height_inches: {self.__height_inches}"


a_person = Person("Shihab", "1997", "5 feet 7 inch")
print(a_person.get_summary())
a_person.set_name("Sajedur Rahman")
print(a_person.get_summary())
