n1 = int(input("Enter a number: "))

# while(n%2 != 0):
#     print("Given number is Prime number ")
#     break

for i in range(2, n1):
    if(n1 % i) == 0:
        print("Number is not prime number")
        break

else:
    print("Number is prime number")