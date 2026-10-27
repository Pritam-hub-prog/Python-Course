a = int(input("Enter a number: "))
b = int(input("Enter the second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey your program is not meant because you divide number by zero")
else:
    print(f"The division is a/b is {a/b}")

