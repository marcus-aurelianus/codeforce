import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


if __name__ == '__main__':
    t= int(input())
    coder = [int(x) for x in input().split()]
    solver = [int(x) for x in input().split()]
    res=0
    c1=0
    c2=0
    for i in range(t):
        if coder[i] and not solver[i]:
            c1+=1
        elif not coder[i] and solver[i]:
            c2+=1
    if c1==0:
        print (-1)
    else:
        print ((c2//c1)+1)

            
