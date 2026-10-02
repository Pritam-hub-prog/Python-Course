num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

# Method1
# if(num1>num2 and num1>num3 and num1>num4):
#     print("Gratest number is num1: ", num1)

# if(num2>num1 and num2>num3 and num2>num4):
#     print("Gratest number is num2: ", num2)

# if(num3>num2 and num3>num1 and num3>num4):
#     print("Gratest number is num3: ", num3)

# if(num4>num2 and num4>num3 and num4>num1):
#     print("Gratest number is num4: ", num4)


# Method 2
if(num1>num2 and num1>num3 and num1>num4):
     print("Gratest number is num1: ", num1)

elif(num2>num1 and num2>num3 and num2>num4):
     print("Gratest number is num2: ", num2)

elif(num3>num2 and num3>num1 and num3>num4):
     print("Gratest number is num3: ", num3)

else:
     print("Gratest number is num4: ", num4)


