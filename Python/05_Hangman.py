again = True
while again == True:
    print("HANGMAN...")

    def split(x):
        return list(x)

    def draw(y):
       a = "string"
       print(a[0:i])
                  
    
    player1 = input("Player1, Enter Your Word: ")
    p1List = split(player1)

    blank = "-"
    blankList = []
    for _ in p1List:
        blankList.append(blank)

    a = 0
    b = 0
    
    while a < len(player1):
        player2 = input("Input the Letters: ")
        for i in p1List:
            if i == player2:
                blankList[p1List.index(i)] = player2
                print(" ".join(blankList))
        else:
            for i in 
                draw(b)
                b = b+1
        a = a+1
