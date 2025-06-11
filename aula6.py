# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# retorne o total para uma variável e mostre o valor
# da variavel.


def multiplicador(*args):
    total = 1
    for numero in args:
        total *= numero

    return total
    

    
multiplicacao = multiplicador(10,2,3,4)

print(multiplicacao)


# Crie uma função fala se número é par ou ímpar.
# retorne se o número é par ou impar

def par_impar(numero):
    return numero % 2 == 0

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

