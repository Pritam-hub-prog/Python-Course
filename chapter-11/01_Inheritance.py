class Employee:  # Base Class
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC infotech"
#     def show(self):
#             print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#             print(f"The name is {self.name} and he is good with {self.language} language")

class Programmer(Employee):  # Derived class
    company = "ITC Info-Tech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)