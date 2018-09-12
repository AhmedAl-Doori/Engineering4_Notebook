import random
l = True
while True:
    print("To Roll the Dice, Press x")
    if input() == "x":
        z = random.randrange(1,7,1)
        print(z)
    else:
        break
