class MinhaClasse:
    def __init__(self):  # metodo construtor
        self.a = 1
        self.b = 2
    
    def soma(self, c = 0):
        return self.a + self.b + c
    
obj = MinhaClasse()


print ('=-' * 50 )
print ('valor da soma',  obj.soma(c=10))
print ('tipo do objeto', type(obj))
print ('=-' * 50 )
