def substituir_letra(string, letra_antiga, letra_nova):
    nova_string = string.replace(letra_antiga, letra_nova)
    return nova_string

texto = "banana"
letra_antiga = "a"
letra_nova = "o"

nova_string = substituir_letra(texto, letra_antiga, letra_nova)
print("String original:", texto)
print("String modificada:", nova_string)
