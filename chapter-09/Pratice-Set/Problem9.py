with open("chapter-9/Pratice-Set/this.txt") as f:
    content = f.read()

with open("chapter-9/Pratice-Set/this_copy.txt") as f:
    content2 = f.read()

if(content == content2):
    print("Yes this is identical matches the content")
else:
    print("No this is not identical matches")