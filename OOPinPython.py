class Person:
    def __init__(self, person_name: str, date_of_birth: int, ht_inches=None):
        self.__name = person_name
        self.__date_of_birth = date_of_birth
        self.__height_inches = ht_inches
        self.abc = None

    def get_year_of_birth(self):
        return self.__date_of_birth

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if(self.__has_any_number(new_name)):
            print("Sorry person name can't have number")
        self.__name = new_name

    def __has_any_number(self, string):
        return "0" in string

    def get_summary(self):
        return f"Name: {self.__name}, DOB: {self.__date_of_birth}, Height_inches: {self.__height_inches if self.__height_inches is not None else 'Invalid'}"


person_list = [Person("Zulakarnine", 1990, 72), Person("foo", 1995), Person(
    "bar", 1998, 72), Person("baz", 1990, 72), Person("ben", 2000, 72)]

for person in person_list:
    if person.get_year_of_birth() >= 1930:
        print(person.get_summary())
