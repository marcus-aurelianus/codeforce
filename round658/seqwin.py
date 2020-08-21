import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())

        arry=list(map(int,input().split()))
        
        res=True
        if arry[0]>1:
            yield 'First'
        else:
            for i in range(1,n):
                res=not res
                if arry[i]!=1:
                    break
            yield 'First' if res else 'Second'

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

