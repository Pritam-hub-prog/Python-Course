f = open("chapter-9/Pratice-Set/poems.txt")
content = f.read()
if("twinkle" in content):
    print("The word Twinkle is present")

else:
    print("The word twinkle is not present")

f.close()