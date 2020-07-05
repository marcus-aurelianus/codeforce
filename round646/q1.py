import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,x = list(map(int,input().split()))
        arry = list(map(int,input().split()))
        
        odd,even=0,0
        for ele in arry:
            if ele%2:
                odd+=1
            else:
                even+=1
        if x<n:
            if even>0:
                if odd>0:
                    yield 'YES'
                else:
                    yield 'NO'
            else:
                if x%2==0:
                    yield 'NO'
                else:
                    yield 'YES'
        else:
            if odd%2==0:
                yield 'NO'
            else:
                yield 'YES'



#7 0                
# 6             
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
