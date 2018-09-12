
while True:
    def myFunction(x,y,z):
        if(z==1):
            return x+y
        elif(z==2):
            return x-y
        elif(z==3):
            return x*y
        elif(z==4):
            return x/y
        elif(z==5):
            return x%y

    a = float(input("Enter first number "))
    b = float(input("Enter second number ")

    print("a + b = {0}".format(myFunction(a,b,1)))
    print("a - b = {0}".format(myFunction(a,b,2)))
    print("a * b = {0}".format(myFunction(a,b,3)))
    print("a / b = {0}".format(myFunction(a,b,4)))
    print("a % b = {0}".format(myFunction(a,b,5)))
    print(" ")
