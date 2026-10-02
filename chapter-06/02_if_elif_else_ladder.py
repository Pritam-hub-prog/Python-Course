age = int(input("Enter your age: "))

# If elif else ladder

if(age>=18):
    print("You are eligible for driving")
    print("Good for you")

elif(age<0):
    print("You enter a negative invalid age")

elif(age==0):
    print("You enter 0 that not a age")
        
else:
    print("You are not eligible for driving")
    

print("End of Program")       