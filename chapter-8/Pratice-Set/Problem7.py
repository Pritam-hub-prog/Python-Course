
def fun(l1, word):
    n = []
    for item in l1:
        if not(item == word):
            n.append(item.strip(word))
    return n
        

l1 = ["moon", "python", "jython", "tn"]

print(fun(l1, "tn"))