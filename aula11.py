
pessoa = {}
chave = 'nome'

pessoa[chave] = 'Matheus Ileck'
pessoa['sobrenome'] = 'Farias'

print(pessoa[chave])

pessoa[chave] = 'Larissa'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('não existe')

else:
    print(pessoa['sobrenome'])