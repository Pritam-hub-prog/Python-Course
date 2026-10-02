with open("chapter-9/Pratice-Set/file.txt") as f:
    content = f.read()

contentNew = content.replace("Donkey", "######")


with open("chapter-9/Pratice-Set/file.txt", "w") as f:
    f.write(contentNew)