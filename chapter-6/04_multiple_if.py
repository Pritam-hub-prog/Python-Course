age = int(input("Enter your age: "))


# IF statement no: 1
if(age%2 == 0):
    print("Age is even")

# End of IF statement no: 1

# IF statement no: 2
if(age>=18):
    print("You are eligible for driving")
    print("Good for you")

elif(age<0):
    print("You enter a negative invalid age")

elif(age==0):
    print("You enter 0 that not a age")
        
else:
    print("You are not eligible for driving")

# End of IF statement no: 2
    

print("End of Program")       