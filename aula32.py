import importlib

import aula32_m

for i in range(10):
    importlib.reload(aula32_m)
    print(i)


print('Fim')