import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        one,two,three = list(map(int,input().split()))
        one1,two1,three1 = list(map(int,input().split()))

        ans = 2*min(three,two1)

        tem=min(three,two1)

        three-=tem
        two1-=tem

        if three1:
            tem1=min(three1,one)
            three1-=tem1
            one-tem1
        if three1 and three:
            tem2=min(three1,three)
            three1-=tem2
            three-=tem2

        ans-=(three1)*2
        yield ans
                
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
