class Fancy(object):

    def __init__(self):
        self.A = []
        self.add = [0]
        self.mul = [1]

    def append(self, a):
        self.A.append(a)
        self.add.append(self.add[-1])
        self.mul.append(self.mul[-1])

    def addAll(self, inc):
        self.add[-1] += inc

    def multAll(self, m):
        self.add[-1] = self.add[-1] * m % (10 ** 9 + 7)
        self.mul[-1] = self.mul[-1] * m % (10 ** 9 + 7)

    def getIndex(self, i):
        print(self.A,self.add,self.mul)
        if i >= len(self.A): return -1
        mod = 10 ** 9 + 7
        m = self.mul[-1] * pow(self.mul[i], mod - 2, mod)
        
        inc = self.add[-1] - self.add[i] * m
        print(i,m,inc,(self.A[i] * m + inc) % mod)
        return (self.A[i] * m + inc) % mod

fancy = Fancy();
fancy.append(2);  
fancy.addAll(3);   
fancy.append(7);   
fancy.multAll(2);  
fancy.getIndex(0); 
fancy.addAll(3);   
fancy.append(10); 
fancy.multAll(2);  
fancy.getIndex(0); 
fancy.getIndex(1); 
fancy.getIndex(2);
