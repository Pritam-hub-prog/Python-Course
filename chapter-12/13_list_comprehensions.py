mylist = [1, 3, 5, 7, 9]

# squredlist = []
# for item in mylist:
#     squredlist.append(item*item)

squredlist = [i*i for i in mylist]  # This called list comprehension

print(squredlist)