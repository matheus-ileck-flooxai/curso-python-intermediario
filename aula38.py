# Exercícios - unir listas
# Crie uma função zipper ( como zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem
# Use todos os valores da menor lista.
# Ex:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
#[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest

def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1),len(lista2))
    return [(lista1[i],lista2[i]) for i in range(intervalo_maximo)]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1,l2))

print(list(zip(l1,l2)))
print(list(zip_longest(l1,l2)))

