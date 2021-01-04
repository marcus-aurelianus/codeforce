import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        candy = list(map(int,input().split()))
        got1 = False
        for ele in candy:
            if ele%2:
                got1=True
                break
        sumD = sum(candy)
        if sumD%2==0:
            if not got1:
                if sumD%4==0:
                    yield 'YES'
                else:
                    yield 'NO'
            else:
                yield 'YES'
        else:
            yield 'NO'
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
