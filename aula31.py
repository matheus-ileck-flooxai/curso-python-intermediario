# Entendendo seus próprios módulos Python
# O primeiro módulo executando chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# ele não reconhece pastas e módulos acima do __main__ por
# padrão
# o python conhece todo os módulos e pacotes presentes
# nos caminhos de sys.path

import aula31_m

print(aula31_m.nome)