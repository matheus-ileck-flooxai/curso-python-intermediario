"""
Escopo de funções em python
Escopo significa o local one aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo logal é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 1 
def escopo():
    x = 10
    def outra_funcao():
        x = 11
        y = 2
        print(x,y) 
    outra_funcao()
    print(x)



print(x)
escopo()
print(x)