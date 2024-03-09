def calcular_frequencia(texto, palavra):
    texto = texto.lower()
    palavras = texto.split()
    frequencia = 0
    for p in palavras:
        if p == palavra.lower():
            frequencia += 1
    return frequencia

texto = "Este é um exemplo de texto. Neste texto, queremos contar quantas vezes a palavra texto aparece."
palavra = "texto"
frequencia = calcular_frequencia(texto, palavra)
print("A palavra '{}' aparece {} vezes no texto.".format(palavra, frequencia))
