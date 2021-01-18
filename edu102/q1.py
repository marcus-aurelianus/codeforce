import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,s = list(map(int,input().split()))
        arr = list(map(int,input().split()))
        arr.sort()
        if n==1:
            if arr[0]>s:
                yield 'NO'
            else:
                yield 'YES'
        else:
            if sum([arr[0],arr[1]])>s and arr[-1]>s:
                yield 'NO'
            else:
                yield 'YES'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
