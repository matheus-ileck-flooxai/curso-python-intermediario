# Funções recursivas e recursividade
# - funções quie podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a execução
# - Fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120

"""
def recursiva(inicio = 0, fim = 4):
    
    print(inicio,fim)

    # Caso base
    if inicio >= fim:
        return fim
    
    # Caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio,fim)

print(recursiva())

"""

def factorial(n):
    if n <= 1 or n <= 0:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))