# EXTERN DATA INSERT
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

# COMPUTING
def maxNum():
    a = (x + y) / 2 + (abs(y - x)) / 2
    b = (y + z) / 2 + (abs(z - y)) / 2
    c = (a + b) / 2 + (abs(b - a)) / 2
    return c
    
n = int(maxNum())

# RETURN
print("O maior inteiro: {:.0f}".format(n))