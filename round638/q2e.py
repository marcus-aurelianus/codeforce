import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k=map(int,input().split())
        lst=list(map(int,input().split()))
        dic={}
        for ele in lst:
            freq=dic.get(ele,0)
            dic[ele]=freq+1
        dlen=len(dic)
        if dlen>k:
            yield -1
        else:

            temps=list(dic.keys())
            tempa=k//dlen*temps+temps[:(k%dlen)]
            tempa.sort()
            ans=tempa*(n)
            yield len(ans)
            yield " ".join(str(x) for x in ans)
 
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
