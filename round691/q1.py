import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input()) 
        a = list(input())
        b = list(input())
        counta=0
        countb=0
        for i in range(n):
            if a[i]>b[i]:
                counta+=1
            elif a[i]<b[i]:
                countb+=1
        #print(counta,countb)
        if counta>countb:
            yield 'RED'
        elif counta<countb:
            yield 'BLUE'
        else:
            yield 'EQUAL'



if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 3 17
# 17 1
