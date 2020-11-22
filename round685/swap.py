import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        a = input()
        b = input()
        dica = defaultdict(lambda:0)
        dicb = defaultdict(lambda:0)
        for i in range(n):
            dica[ord(a[i])-ord('a')]+=1
            dicb[ord(b[i])-ord('a')]+=1
        
        ans = True
        indexa = 0
        indexb = 0

        for indexa in range(26):
            
            if dica[indexa]:
                
                for indexb in range(indexa,26):
                    if dicb[indexb]:
                        if indexb==indexa:
                            toMinus = min(dicb[indexb],dica[indexa])
                        else:
                            toMinus = min(dicb[indexb],dica[indexa])-min(dicb[indexb],dica[indexa])%k
                        dicb[indexb]-=toMinus
                        dica[indexa]-=toMinus
        #print(dica,dicb)
        ans = True
        for indexa in range(26):
            if dica[indexa]:
                ans = False
                
        yield 'YES' if ans else 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
