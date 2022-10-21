import math

num = int(input("Valor: "))

cem = num // 100
res1 = num - 100 * cem
cinquenta = res1 // 50
res2 = res1 - 50 * cinquenta
vinte = res2 // 20
res3 = res2 - 20 * vinte
dez = res3 // 10
res4 = res3 - 10 * dez
cinco = res4 // 5
res5 = res4 - 5 * cinco
dois = res5 // 2
res6 = res5 - 2 * dois
um = res6 // 1
res7 = res6 - um

print('{} de 100, {} de 50, {} de 20, {} de 10, {} de 5, {} de 2, {} de 1'.format(cem, cinquenta, vinte, dez, cinco, dois, um))