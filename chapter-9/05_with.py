f = open("chapter-9/file.txt")
print(f.read())
f.close()

# This same can be written using with statement like this:
with open("chapter-9/file.txt") as f:
    print(f.read())

# You dont have to close the file it automatically close because we use with statement here.