class animals:
    pass

class pets(animals):
    pass

class dogs(pets):

    @staticmethod
    def bark():
        print("Bow Bow!")

c = dogs()
c.bark()