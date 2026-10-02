# Using recursion 
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(3)

# Withot use recursion we write this program like this:(use for loop)
def pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

pattern(3)

# Withot use recursion we write this program like this:(use while loop)
def pattern(n):
    while (n > 0):
        print("*" * n)
        n = n - 1

pattern(3)