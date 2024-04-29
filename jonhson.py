from uteis import *
from sat import *

def aleatorio(V):
    for v in V:
        v.set(randp(1/2))


def EspCond(v, i, D):
    esp = 0

    for c in D:
        k = len(c.c1) + len(c.c0)

        if(c.contem(v, bool(i))):
            esp = esp + 1

        elif (c.contem(v, bool(i-1))):
            esp = esp + (1 - 2**(-k + 1))
        
        else:
            esp = esp + (1 - 2**(-k))
    
    return esp


def nao_aleatorio(V, C):
    D = C

    for v in V:
        if EspCond(v, 1, D) >= EspCond(v, 0, D):
            v.set(True)

            for c in D:
                if(c.contem(v, False)):
                    D.remove(c)
                
                else:
                    c.c0.remove(v)
    
        else:
            v.set(False)

            for c in D:
                if(c.contem(v, True)):
                    D.remove(c)
                
                else:
                    c.c1.remove(v)

