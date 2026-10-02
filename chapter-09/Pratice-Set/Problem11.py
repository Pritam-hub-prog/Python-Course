with open("chapter-9/Pratice-Set/old.txt") as f:
    content = f.read()

with open("chapter-9/Pratice-Set/renamed_by_python.txt", "w") as f:
    f.write(content)

