import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry=list(map(int,input().split()))

        res=0
        for i in range(1,n):
            diff=arry[i]-arry[i-1]
            if diff<0:
                valtoaad=abs(diff)
                kap=bin(valtoaad)[2:]
                m=len(kap)

                temp=res^valtoaad
                if temp:
                    res+=temp
                    
                else:
                    res+=2**(m)
                arry[i]+=valtoaad
                print(valtoaad)
        print(arry)       
        if res:  
            yield len(bin(res)[2:])
        else:
            yield 0
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
