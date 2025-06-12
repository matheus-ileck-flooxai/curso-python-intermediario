# dir, hasattr e getattr em Python
string = 'Matheus'
metodo = 'upper'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não exisitie o método', metodo)