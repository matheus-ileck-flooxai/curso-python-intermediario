# copy, sorted, produtos.sortAdd commentMore actions
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy


def aplica_dez_porcento_aumento(numero):
    porcentagem = (numero * 100) / 1000
    numero_com_aumento = numero + porcentagem
    return round(numero_com_aumento,2)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
novos_produtos = copy.deepcopy(produtos)

novos_produtos = [
    {**produto, 'preco': aplica_dez_porcento_aumento(produto['preco']) }
    for produto in produtos
]


print('Lista original \n ', produtos)

print('Novos produtos \n ', novos_produtos)


# Ordene os produtos por nome decrescente (do maior para menor)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda p: p['nome'],
    reverse=True
)

print('Sorted por nome decrescente \n ', produtos_ordenados_por_nome)



# Ordene os produtos por preco crescente (do menor para maior)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda p: p['preco'],
)

print('Sorted por preco \n ', produtos_ordenados_por_preco)

