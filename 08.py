import random

def embaralhar(lista):
    lista_embaralhada = lista[:]
    
    random.shuffle(lista_embaralhada)
    
    return lista_embaralhada

minha_lista = [1, 2, 3, 4, 5]
print("Lista original:", minha_lista)

lista_embaralhada = embaralhar(minha_lista)
print("Lista embaralhada:", lista_embaralhada)
