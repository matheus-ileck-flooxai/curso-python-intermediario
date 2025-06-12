# Introdução às Generator function em Python
# generator = (n for n in range(100000))

def generator(n=0):
    yield 1 #Pausar
    print('Continuando...')
    yield 2
    print('Mais uma vez...')
    yield 3
    print('Acabou')
    return 'Acabou'


gen = generator(n=0)
for n in gen:
    print(n)
