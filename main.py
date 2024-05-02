import jonhson
from instancia import *
MAX_I = 100


V,C = ler_entrada('teste1.wcnf')


max = 0
for j in range(MAX_I):
    jonhson.aleatorio(V)

    i = 0
    for c in C:
        if c.avaliar():
            i = i + 1
    
    if i > max:
        max = i

print("Com o aleatorio: " + str(max))

ler('teste1log.wcnf', V)

i = 0
for c in C:
    if c.avaliar():
        i = i + 1

print("Com o log: " + str(i))


'''
jonhson.nao_aleatorio(V, C)

i = 0
for c in C:
    if c.avaliar():
        i = i + 1


print("Com o nao aleatorio: " + str(i))
'''