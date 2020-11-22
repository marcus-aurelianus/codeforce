import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        if n==1:
            yield 0
        elif n==2:
            yield 1
        elif n==3:
            yield 2

        elif n%2:
            yield 3
        else:
            yield 2
                
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
