import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        h = list(map(int,input().split()))
        ans=True
        minV,maxV = h[0],h[0]
        for i in range(1,n):
            maxV = min(h[i]+k-1 , maxV+k-1)
            minV = max(h[i] , minV-k+1)
     
     
            if maxV < minV:
                ans=False
                break

            
        if not ans:
            yield 'NO'
        else:
            if minV<=h[-1]<=maxV:
                yield 'YES'
            else:
                yield 'NO'
            

        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
