class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name} and i am {self.age} years old"

s = Student("Pritam", 21)

print(s)