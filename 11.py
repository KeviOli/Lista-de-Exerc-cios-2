def is_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2
    return True

def numeros_primos(lista):
    primos = []
    for numero in lista:
        if is_primo(numero):
            primos.append(numero)
    return primos

numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primos = numeros_primos(numeros)
print("Números primos na lista:", primos)
