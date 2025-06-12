# isinstance - para saber se o objeto é de determinado tipo
lista = [
    'a', 1,1.1, True, [0,1,2], (1,2),
    {0,1},{'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item,set):
        print('SET')
        print(item, isinstance(item,set))
    elif isinstance(item, str):
        print('STR')
        item.upper()
        print(item, isinstance(item,str))

    elif isinstance(item, (int,float)):
        print('NUM')
        print(item, item * 2)
    else:
        print('Outro')
