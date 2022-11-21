#numeros iguales o diferentes
def  iguales(n1,n2,n3):

    if (n1 == n2 == n3):
        return("los 3 numeros son iguales")
    elif (n1 == n2 != n3):
        return("dos numeros son iguales")
    elif (n3 == n2 != n1):
        return("dos numeros son iguales")
    elif (n3 == n1 != n2):
        return("dos numeros son iguales")
    else:
        return("ningun numero es igual")
    
n1 = float(input("introduzca un numero: "))
n2 = float(input("introduzca un numero: "))
n3 = float(input("introduzca un numero: "))
print (iguales(n1,n2,n3))