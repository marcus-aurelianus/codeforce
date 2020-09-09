import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

            
def gift():
    for _ in range(t):
        n = int(input())
        arry = list(map(int,input().split()))

        if n == 1:
            yield 'T'
        elif n==2:
            if arry[0]!=arry[1]:
                yield 'T'
            else:
                yield 'HL'
        else:
            sumN = sum(arry)
            maxNum  = max(arry)
            if maxNum > sumN - maxNum:
                yield "T"
            else:
                if sumN % 2:
                    yield 'T'
                else:
                    yield 'HL'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')


#1 3 2 4
#1 12 8 12
#4 


# 11 10 9 8

# 0 6 5 5
# 6 5 5
# 6 1 1 
# 
