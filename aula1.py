"""
Introdução as funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
""" 

def saudacao(nome='Sem Nome'):
    print(f'Olá {nome}')


saudacao('Matheus')