"""
Higher Order Functions
Funções de primeira classe

"""


def saudacao(msg):
    return msg


def executa(funcao, texto):
    return funcao(texto)


v = executa(saudacao,'Bom dia')
print(v)