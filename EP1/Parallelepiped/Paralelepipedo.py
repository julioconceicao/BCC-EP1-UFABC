import math as mt

#EXTERN DATA INSERTS
e1 = int(input("Edge 1: ")) 
e2 = int(input("Edge 2: "))
e3 = int(input("Edge 3: "))

#VOLUME COMPUTATION
Vol = e1 * e2 * e3

#DIAGONAL COMPUTATION
Diagonal = mt.sqrt(e1 ** 2 + e2 ** 2 + e3 ** 2)

#RETURN
print("Vol: {:.2f}".format(Vol))
print("Diagonal: {:.2f}".format(Diagonal))
