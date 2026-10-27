with (
    open("chapter-12/file1.txt", "r+") as f1,
    open("chapter-12/file2.txt", "r+") as f2
):
    print(f1.read())
    print(f2.read())

    f1.write("This course is helpful")
    f2.write("now we use basically 3.14 python")
    