with open("chapter-9/Pratice-Set/log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Python is available on line no.: {lineno}")
        break
    lineno += 1

else:
    print("Python is not available")