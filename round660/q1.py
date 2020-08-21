import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__



def gift():
    for _ in range(t):
        n = int(input())
        if n>=31:
            yield 'YES'
            if n in [36,40,44]:
                yield "6 10 15 {}".format(n-31)
            else:
                yield "6 10 14 {}".format(n-30)
        else:
            yield 'NO'
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 80000
