again = True
while again == True:
    
    print("THE SPLITTER PROGRAM")

    choice = input("Would you like to 'split' or 'seperate'? ")
    sentence = input("Enter your sentence: ")

    def split(a):
        return print(a.split(" "))

    def seperate(b):
        for letter in b:
            if letter == " ":
                print("-")
            else:
               print(letter)

    if choice == "split":
        split(sentence)
    elif choice == "seperate":
        seperate(sentence)
    else:
        print("I can't do that")

    end = input("Go Again? (Y/N) ")
    if end == "N":
        again = False
    else:
        again = True
