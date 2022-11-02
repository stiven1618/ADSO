def el_numero_es_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma == numero

print(el_numero_es_perfecto(487))