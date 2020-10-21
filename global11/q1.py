import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        array = list(map(int,input().split())) 

        sumA = sum(array)

        if sumA == 0:
            yield 'NO'
        else:
            yield 'YES'
            if sumA>0:
                ans =  sorted(array,reverse=True)
            else:
                ans =  sorted(array)
            yield " ".join(str(x) for x in ans)
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
