import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        ans = []

        for i in range(n//2+n%2):
            if n%2 and i==(n//2+n%2-1):
                ans.append(array[i])
            else:
                ans.append(array[i])
                ans.append(array[n-1-i])
        yield " ".join([str(x) for x in ans])
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
