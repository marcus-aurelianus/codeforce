import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b,x,y = [int(x) for x in input().split()]
        s1=a*(b-y-1)
        s2=a*(y)
        s3=b*(a-x-1)
        s4=b*x
        yield max([s1,s2,s3,s4])
        
        

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
