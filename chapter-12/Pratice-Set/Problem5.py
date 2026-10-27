n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
with open("chapter-12/Pratice-Set/tables.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")