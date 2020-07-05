import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        arry = list(map(int,input().split()))
        odd=[]
        even=[]
        tochange=[]
        for i in range(n):
            if i%2!=arry[i]%2:
                if i%2:
                    odd.append(i)
                else:
                    even.append(i)
      
        z=len(odd)
        x=len(even)
        #yield odd,even
        if z!=x:
            yield -1
        else:
            yield z
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
