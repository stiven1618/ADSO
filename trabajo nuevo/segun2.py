def sumaDivisores(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma+=i
    return suma
def primos(num):
    sum=sumaDivisores(num)
    if sum==1:
        return'es primo'
    else:
        return'no es primo'
    
print(primos(11))



















###hacer una funcion para determinar que numero es primo