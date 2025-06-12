# Empacotamento e desempatocamento de dicionários
a, b = 1, 2
a, b = b, a

# print(a,b)

# (a1, a2), (b1, b2) = pessoa.item()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.item():
# print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.65,
}

pessoas_completa = {**pessoa, **dados_pessoa}

# args e kwargs
# args (argumentos não nomeados)
# kwargs - keyhword argumento ( argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados', args)
    for chave, valor in kwargs.items():
        print(chave,valor)


mostro_argumentos_nomeados(nome='Matheus', idade=16)