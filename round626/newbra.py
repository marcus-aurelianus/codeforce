import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


if __name__ == '__main__':
    n=int(input())
    brackets=input()

    wrongbra=0
    tl,tr=0,0
    l,r=0,0
    wrongNow=False
    for i,bra in enumerate(brackets):
        if bra==")":
            r+=1
            tr+=1
        else:
            l+=1
            tl+=1
        if l<r:
            wrongNow=True
        if wrongNow:
            if l==r:
                wrongNow=False
                wrongbra+=(l+r)
                l,r=0,0
        else:
            if l==r:
                l,r=0,0
    if tl!=tr:
        print(-1)
    else:
        print(wrongbra)
