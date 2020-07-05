import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        string=input()
        res=[]
        for i in range(k//2+k%2):
            res.append({})

        for i in range(n//k):
            for j in range(k//2+k%2):
                #print(res,j)
                freq=res[j].get(string[i*k+j],0)
                res[j][string[i*k+j]]=freq+1
                if k%2!=0 and j==k//2+k%2-1:
                    continue
                else:
                    freq=res[j].get(string[(i+1)*(k)-j-1],0)
                    res[j][string[(i+1)*(k)-j-1]]=freq+1
        ans=0
        for i in range(k//2+k%2):
            each=res[i]
            maxval=each[max(each, key=each.get)]
            if k%2!=0 and i==k//2+k%2-1:
                ans+=(n//k-maxval)
            else:
                ans+=(n//k*2-maxval)
        #yield res
        yield ans

        
    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')

