class Employee:
    language = "Python"  
    salary = 15000000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating a object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

pritam = Employee("Pritam Patra", 18000000, "Java script")
print(pritam.name, pritam.salary, pritam.language)

# pritam.name = "Pritam Patra"
# piyush = Employee()

# A dunder method is start from double underscore e.g (__init__, __str__)

 