l = [101, 102, 103, 104, 105, 106, 107, 108]

# for index, item in enumerate(l):
#           if (index == 2):
#                  print(f"The item at {index} position and the item is {item}")

#           elif (index == 4):
#                    print(f"The item at {index} position and the item is {item}")
#           elif (index == 6):
#                    print(f"The item at {index} position and the item is {item}")

# This program also do in this process

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
         print(f"The item at {i} position and the item is {item}") 

                  