from sat import *

def ler_entrada(entrada):
    wcnf = open(entrada, 'r')

    V = []
    C = []

    for linha in wcnf:
        if(linha[0] == 'p'):
            l = linha.split(' ')

            for i in range(int(l[2])):
                V.append(Variavel(False))
        
        elif(linha[0] == 'h' or linha[0] == '1'):
            l = linha.split(' ')

            c0 = []
            c1 = []

            i = 1

            while(l[i] != '0\n' and l[i] != '0'):
                if l[i][0] == '-':
                    c0.append(V[int(l[i].replace('-', '')) - 1])
                else:
                    c1.append(V[int(l[i])-1])
                
                i = i + 1


            C.append(Clausula(c0,c1))


    return (V, C)

def ler(entrada, V):

    wcnf = open(entrada, 'r')
    i = 0

    for linha in wcnf:
        if linha[0] == 'v':

            for l in linha:
                if(l == '0'):
                    V[i].valor = False
                    i = i + 1
                elif(l == '1'):
                    V[i].valor = True
                    i = i + 1
                
                

                    

