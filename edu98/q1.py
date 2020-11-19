import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        x,y = list(map(int,input().split()))
        if abs(x-y)==0:
            yield x*2
        else:
            yield abs(x-y)*2-1+min(x,y)*2
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
