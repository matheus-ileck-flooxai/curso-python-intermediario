#Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
     {
        'Pergunta': 'Quanto é 5x5',
        'Opções': ['25', '40', '10', '51'],
        'Resposta': '25',
    },
     {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['1', '5', '4', '6'],
        'Resposta': '5',
    },
    
]

respostas_corretas = 0
for pergunta in perguntas:

    print(f'Pergunta: {pergunta['Pergunta']}')

    opcoes = pergunta['Opções']

    for opcao in opcoes:
        print(f'{opcao}')

    resposta = input('Escolha uma opção: ')

    if resposta == pergunta['Resposta']:
        respostas_corretas += 1


print(f'Você acertou {respostas_corretas} respostas')