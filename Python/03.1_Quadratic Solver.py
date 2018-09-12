print("Quadratic Solver")
print("Input coefficients ax^2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

def discriminant(x,y,z):
    return y**(2)-(4*x*z)
    
d = discriminant(a,b,c)
if d < 0:
    print("NO REAL SOLUTIONS")
else:
    solutions = [ (-b + d**(1/2))/(2*a),(-b - d**(1/2))/(2*a)]
    if solutions[0] != solutions[1]:
        print("The first solution is: {0}".format(solutions[0]))
        print("The second solution is: {0}".format(solutions[1]))
    else:
        print("The ONLY solution is: {0}".format(solutions[0]))
