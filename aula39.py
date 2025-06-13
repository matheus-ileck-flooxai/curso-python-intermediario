def soma_listas(l1,l2):
    intervalo_maximo = min(len(l1),len(l2))
    return [(l1[i] + l2[i]) for i in range(intervalo_maximo)]

l1 = [1,2,3,4,5,6,7]

l2 = [2,4,6,8]

print(soma_listas(l1,l2))