def menor_string(lista):
    if not lista:
        return None
    
    menor = lista[0]
    
    for string in lista:
        if len(string) < len(menor):
            menor = string
            
    return menor

lista_de_strings = ["maçã", "banana", "laranja", "abacaxi", "uva"]
menor = menor_string(lista_de_strings)
print("A menor string na lista é:", menor)
