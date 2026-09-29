import random


computer = random.choice([1, -1, 0])
yourString = input("Enter your Choice: ")
yourDict = {"s": 1, "w": -1, "g": 0}
reversDict = {1: "Snake", -1: "Water", 0: "Gun"}
yourNum = yourDict[yourString]

print(f"You choose {reversDict[yourNum]}\nComputer choose {reversDict[computer]}")

if(computer == yourNum):
    print("Game Draw")
    
else:
    '''
     if(computer == -1 and yourNum == 1):  (computer - you) = -2
            print("You win")
    
     elif(computer == -1 and yourNum == 0): (computer - you) = -1
            print("You Lose")
    
    elif(computer == 1 and yourNum == -1):  (computer - you) = 2
            print("You Lose")
    
    elif(computer == 1 and yourNum == 0):  (computer - you) = 1
            print("You Win")
    
    elif(computer == 0 and yourNum == 1):  (computer - you) = -1
            print("You Lose")
    
    elif(computer == 0 and yourNum == -1):  (computer - you) = 1
            print("You Win")

    The below logic is written on the basic of the value of the (computer - 1). 
    
    '''


    if((computer - yourNum) == -1 or (computer - yourNum) == 2):
        print("You Lose")
    else:
        print("You win")