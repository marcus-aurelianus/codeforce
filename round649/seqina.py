import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry = list(map(int,input().split()))

        ans=[arry[0]]

        pm='not'
        for i in range(n-1):
            currele=arry[i+1]
            prevele=arry[i]
            

            if pm=='not':
                if currele>prevele:
                    pm='plus'
                else:
                    pm='minus'
            else:
                if currele>prevele:
                    curpm='plus'
                else:
                    curpm='minus'
                if curpm!=pm:
                    ans.append(arry[i])
                    pm=curpm
            if i==n-2:
                ans.append(arry[n-1])
        yield len(ans)
        yield " ".join(str(x) for x in ans)
                    

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
