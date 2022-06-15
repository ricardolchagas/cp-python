a = 1
b = 1

print (a)
for b in range(1, 10):    
    pass

print (a)

while a < 10:
    if  a == b:
        print('a é igual a b')
        print ("parte do verdadeiro")
        a = 2
    
    print (a)
    a = a + 1
        
print ("fora do if")


class MinhaClasse:
    def __init__(self):  # metodo construtor
        self.a = 1
        self.b = 2
    
    def soma(self):
        return self.a + self.b


