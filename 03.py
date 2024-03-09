def contar_palavras(string):
    palavras = string.split()
    
    return len(palavras)

texto = "salve salve familia"
print("Número de palavras:", contar_palavras(texto))
