def contar_vogais(string):
    num_vogais = 0
    
    vogais = 'aeiouAEIOU'
    
    for char in string:
        if char in vogais:
            num_vogais += 1
    
    return num_vogais

texto = "EU SOU O BATMAN."
print("Número de vogais:", contar_vogais(texto))
