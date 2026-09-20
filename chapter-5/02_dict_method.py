marks = {
    "Pritam": 100,
    "moon": 99,
    "Ayush": 98,
    "piyush": 97,
    1: "Pritam"

}
print(len(marks))

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Pritam": 90, "Manis": 100})
# print(marks)
# print(marks.get("Pritam")) # If this key doesnt exit in the dictonary then its give none.
# print(marks["Pritam"])  # If this key doesnt exit in the dictionary it returns error.
marks.pop("Pritam", 100)
print(marks)

items = marks.popitem()  # It shows which item is pop 
print(items)  