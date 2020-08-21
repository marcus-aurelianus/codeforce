import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        r,g,b,w = list(map(int,input().split()))
        odd=0

        for ele in [r,g,b,w]:
            if ele%2:
                odd+=1
        if odd<=1:
            yield 'Yes'
        else:
            minm=min(r,g,b)
            if minm==1:
                odd=0
                for ele in [r-1,g-1,b-1,w+3]:
                    if ele%2:
                        odd+=1
                if odd<=1:
                    yield 'Yes'
                else:
                    yield 'No'
            elif minm>=2:
                odd1=0
                for ele in [r-1,g-1,b-1,w+3]:
                    if ele%2:
                        odd1+=1
                odd2=0
                for ele in [r-2,g-2,b-2,w+6]:
                    if ele%2:
                        odd2+=1
                if odd1<=1 or odd2<=1:
                    yield 'Yes'
                else:
                    yield 'No'
            else:
                yield 'No'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
