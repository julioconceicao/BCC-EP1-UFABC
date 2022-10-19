import math as mt

#EXTERNAL DATA INSERTS
ray = int(input("Insert circumference ray: "))

#AREA COMPUTATION
area = mt.pi * mt.pow(ray, 2)

#RETURN
print("Circumference area {:.4f}".format(area))