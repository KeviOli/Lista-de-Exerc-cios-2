def k_maiores(lista, k):
    lista_ordenada = sorted(lista, reverse=True)
    
    k_maiores_elementos = lista_ordenada[:k]

    k_maiores_elementos_ordem_original = []
    for elemento in lista:
        if elemento in k_maiores_elementos:
            k_maiores_elementos_ordem_original.append(elemento)
    
    return k_maiores_elementos_ordem_original

lista = [4, 8, 2, 6, 3, 9, 1, 5, 7]
k = 3
print("Os", k, "maiores elementos na lista são:", k_maiores(lista, k))
