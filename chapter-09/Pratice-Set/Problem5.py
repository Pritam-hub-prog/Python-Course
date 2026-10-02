words = ["Donkey", "bad", "good"]
with open("chapter-9/Pratice-Set/file.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))


with open("chapter-9/Pratice-Set/file.txt", "w") as f:
    f.write(content)