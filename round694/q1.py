import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b,c = list(map(int,input().split()))
        yield a+b+c-1

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)



# 1 x 1 x 1
# 1 1 1 1 1
# y 1 1 1 y
# 1 1 1 1 1
# 1 x 1 x 1
