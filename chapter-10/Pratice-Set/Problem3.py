class new:
    a = 10

newObj = new()
print(newObj.a) # Prints the class attribute because instance attribute is not present

newObj.a = 0
print(newObj.a) # Prints the instance attribute because the instance attribute is presemt

print(new.a) # Print the class attribute