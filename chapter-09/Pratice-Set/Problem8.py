with open("chapter-9/Pratice-Set/this.txt") as f:
    content = f.read()

with open("chapter-9/Pratice-Set/this_copy.txt", "w") as f:
    f.write(content)