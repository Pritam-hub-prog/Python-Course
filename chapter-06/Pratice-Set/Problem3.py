p1 = "Make a lot of money"
p2 = "buy now"
p3 = "suscribe this"
p4 = "click this"

mesg = input("Enter your comment: ")

if((p1 in mesg) or (p2 in mesg) or (p3 in mesg) or (p4 in mesg)):
    print("This comment is spam")

else:
    print("This comment is not a spam")