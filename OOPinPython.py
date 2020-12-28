class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


a_person = Person("Shihab")
b_person = Person("Robot")

print(a_person.get_name())
print(b_person.get_name())
