def determinar_divisores(numero):
    '''determinar los divisores de un numero'''
    divisores = []
    for i in range(1, numero+1):
        if numero % i == 0:
            divisores.append(i)
    return divisores
d = determinar_divisores(111)
print(d)