#EXTERN DATA INSERT
name = str(input("Primeiro nome do vendedor: "))
fixWage = float(input("Salário fixo: "))
totalSales = float(input("Total de vendas em dinheiro: "))

#TOTALWAGE COMPUTATION
totalWage = fixWage + (0.05 * totalSales)

#RETURN
print("{} ".format(name) + "deve receber {:.2f}".format(totalWage))
