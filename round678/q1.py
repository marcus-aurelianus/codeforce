import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,s = list(map(int,input().split()))
        array = list(map(int,input().split()))
        if sum(array) == s:
            yield 'YES'
        else:
            yield 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
