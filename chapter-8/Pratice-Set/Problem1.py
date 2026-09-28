def great():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    if(a > b and c):
        print("The gratest number is : ", a)

    elif(b > c and a ):
        print("The gratest number is : ", b)

    else:
        print("The gratest number is : ", c)

great()

# Another way for this when the number is available
def gratest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a = 23
b = 6
c = 123

print("The gratest number is:",gratest(a, b, c))

# 2nd Another way
def gratest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

fin = gratest(2, 56, 6)
print(fin)