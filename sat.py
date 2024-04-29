class Variavel:

    def __init__(self, v):
        self.valor = v

    def set(self, v):
        self.valor = v



class Clausula:

    def __init__(self):
        self.c0 = []
        self.c1 = []
    
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
    
    def append(self, variavel, barrado):
        if barrado:
            self.c0.append(variavel)
        else:
            self.c1.append(variavel)

    def avaliar(self):

        for i in self.c0:
            if not i.valor:
                return True;

        for i in self.c1:
            if i.valor:
                return True;    

        return False;

    def contem(self, v, barrado):

        if barrado:
            for i in self.c0:
                if i == v:
                    return True
            
            return False

        else:
            for i in self.c1:
                if i == v:
                    return True
            
            return False


    def printar(self):
        res = ''

        for i in self.c0:
            res = res + str(not i.valor) + " V "
        
        for i in self.c1:
            res = res + str(i.valor) + " V "
        
        print(res)


a = Variavel(False)
b = Variavel(True)

C = Clausula([a],[b])

print("'a' está em c0: " + str(C.contem(a, True)))
print(" 'a' está em c1: " + str(C.contem(a, False)))

print("'b' está em c0: " + str(C.contem(b, True)))
print(" 'b' está em c1: " + str(C.contem(b, False)))