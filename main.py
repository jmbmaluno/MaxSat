import jonhson
from sat import *

a = Variavel(False)
b = Variavel(False)
c = Variavel(False)
d = Variavel(False)
e = Variavel(False)
f = Variavel(False)

C1 = Clausula([a], [b,c])
C2 = Clausula([b,c], [d])
C3 = Clausula([e,a], [f,b,c])

V = [a,b,c,d,e,f]

C = [C1,C2,C3]

'''
jonhson.aleatorio(V)

i = 0
for c in C:
    if c.avaliar():
        i = i + 1

print("Com o aleatorio: " + str(i))

'''
jonhson.nao_aleatorio(V, C)

i = 0
for c in C:
    if c.avaliar():
        i = i + 1


print("Com o nao aleatorio: " + str(i))
