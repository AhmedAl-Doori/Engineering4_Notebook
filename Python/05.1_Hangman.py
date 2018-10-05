print("HANGMAN")

player1 = input("Enter the secret word: ")
p1List = list(player1) #convert input to list

blankList = []
for _ in p1List:
    blankList.append("-") #create empty list

c = 0
while c < 35:
    print(" \n")
    c = c+1 #the quick scroll

print("There are {} letters".format(len(p1List)))    
print(blankList)

a = 0 # The scanning counter
b = 1 # The mistakes coutner




def draw(x):
    drawArray = ["-------",
                 "      |",
                 "      |",
                 "      |",
                 "      O",
                 "     /U|",
                 "      |",
                 "     / |"
                 ]
    for item in drawArray[0:x]:
        print(item)
        
while b < 8:
    correct = False
    player2 = input("\n Enter your guess: ")

    for index,item in enumerate(p1List):
        if item == player2:
            blankList[index] = player2
            correct = True
    
    print(blankList)
    
    if not correct:
        b = b+1
        draw(b)

    if blankList == p1List:
        print("GOOD JOB! GAME OVER")
        break
