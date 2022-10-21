import math as mt
#EXTERN DATA INSERT
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
x = float(input("x: "))

# COMPUTE FIRST ROOT VALUE
def i():
    return (-b + mt.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)

# COMPUTE SECOND ROOT VALUE
def ii():
    return (-b - mt.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
    
# COMPUTE SECOND DEGREE EQ.
def iii():
    return a * pow(x, 2) + b * x + c

# RETURN
print("raizes: {:.2f} {:.2f}".format(i(), ii()), "resultado para x = {:.2f}: {:.2f}".format(x, iii()))
