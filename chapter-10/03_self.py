class Employee:
    language = "Python" 
    salary = 15000000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

pritam = Employee()
pritam.language = "Java Script" 
pritam.getInfo()
pritam.greet()
# Employee.getInfo(pritam)

# self : The same method can work with different objects.
 