from functools import partial
from types import GeneratorType


#map para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 4', 'preco': 105.87},
    {'nome': 'Produto 2', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem)

novos_produtos = filter(
    lambda p: p['preco'] >= 10,
    produtos
)

print_iter(novos_produtos)
