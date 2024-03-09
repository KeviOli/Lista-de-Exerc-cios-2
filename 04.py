def contar_ocorrencias(frase, palavra):
    palavras = frase.split()
    
    num_ocorrencias = 0
    
    for p in palavras:
        if p == palavra:
            num_ocorrencias += 1
    
    return num_ocorrencias

frase = "sim batman eu sou o batman "
palavra = "batman"
print("Número de ocorrências da palavra:", contar_ocorrencias(frase, palavra))
