with open("chapter-9/Pratice-Set/log.txt") as f:
    content = f.read()
       
if("python" in content):
    print("Python is available")
else:
    print("Python is not available")