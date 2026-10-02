class Employee:
    language = "Py"  # This is a class attribute
    salary = 15000000

pritam = Employee()
pritam.name = "Pritam Patra"  # This is an instance attribute
print(pritam.name, pritam.salary, pritam.language)

durga = Employee()
durga.name = "Dudu prasad"
print(durga.name, durga.salary, durga.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class 