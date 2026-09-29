'''

1 for snake
-1 for water
0 for gun

'''
import random


computer = random.choice([1, -1, 0])
yourString = input("Enter your Choice: ")
yourDict = {"s": 1, "w": -1, "g": 0}
reversDict = {1: "Snake", -1: "Water", 0: "Gun"}
yourNum = yourDict[yourString]

# By now we have two numbers , you and computer 

print(f"You choose {reversDict[yourNum]}\nComputer choose {reversDict[computer]}")


if(computer == yourNum):
    print("Game Draw")

else:
    if(computer == -1 and yourNum == 1):
        print("You win")

    elif(computer == -1 and yourNum == 0):
        print("You Lose")

    elif(computer == 1 and yourNum == -1):
        print("You Lose")

    elif(computer == 1 and yourNum == 0):
        print("You Win")

    elif(computer == 0 and yourNum == 1):
        print("You Lose")

    elif(computer == 0 and yourNum == -1):
        print("You Win")

    else:
        print("Something Went Wrong")

    