import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n, k = list(map(int,input().split()))
        seq = input()
        dic = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',
               7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',
               15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',
               23:'x',24:'y',24:'z'}
        picked = defaultdict(lambda:False)
        ans = [0]*n
        for i in range(n):
            curSeq = ord(seq[i])-ord('a')
            if not picked[i] and (curSeq==k-1 or currSeq==0):
                ans[0]='a'
                picked[i]=True
            else:
                if i+2<=n-1:
                    n1Seq = ord(seq[i+1])-ord('a')
                    n2Seq = ord(seq[i+2])-ord('a')
                    
                elif i+1<=n-1:
                    n1Seq = ord(seq[i+1])-ord('a')
                    if 
            
            picked[i]=1
        
        yield picked,ans
                        
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)


#baccacd
#aabdac
