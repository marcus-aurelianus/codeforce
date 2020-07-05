import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        num=int(input())
        if (num//2-1)%2:
            yield 'YES'
            firsthalf=list(map(lambda x:x*2,range(1,num//2+1)))
            secondhalf=list(map(lambda x:x*2-1,range(1,num//2)))
            ans=firsthalf+secondhalf+[num*3//2-1]
            yield " ".join(str(x) for x in ans)
        else:
            yield 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
 
