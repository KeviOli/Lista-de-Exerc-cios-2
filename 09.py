def encontrar_par_soma(lista, valor_alvo):
    pares = []
    conjunto_lista = set(lista)
    
    for elemento in lista:
        diferenca = valor_alvo - elemento
        
        if diferenca in conjunto_lista:
            pares.append((elemento, diferenca))
    
    return pares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
valor_alvo = 10
pares = encontrar_par_soma(lista, valor_alvo)

if pares:
    print("Pares cuja soma é igual a", valor_alvo, ":", pares)
else:
    print("Não há pares na lista cuja soma é igual a", valor_alvo)
