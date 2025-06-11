"""
Dicionários em python (tipo dict)
Dicionários são estruturas de dados do tipo
par de chave "chave" e "valor".
Chaves podem ser consideradas como o "Índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves {} ou a classe dict pra criar dicionarios.
Imutaveis: str, int, float, bool, tuple
Mutaveis: dict,list
"""

pessoa = {
    'nome': 'Matheus Ileck',
    'sobrenome': 'Farias',
    'idade': 23,
    'altura': 1.85,
    'endereco': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}

print(pessoa)