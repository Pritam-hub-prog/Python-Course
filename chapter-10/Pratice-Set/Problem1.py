class programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

employee1 = programmer("Pritam", 150000, 7550)
print(employee1.company, employee1.name, employee1.salary, employee1.pin)

employee2 = programmer("Harsh", 140000, 7560)
print(employee2.company, employee2.name, employee2.salary, employee2.pin)

employee3 = programmer("Shubham", 130000, 7570)
print(employee3.company, employee3.name, employee3.salary, employee3.pin)


