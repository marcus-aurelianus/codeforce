import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        arrayA = list(map(int,input().split()))
        arrayB = list(map(int,input().split()))
        arrayC = list(map(int,input().split()))
        res = [arrayA[0]]

        for i in range(1,n):
            if i == n-1:
                tem = [res[i-1],res[0]]
                if arrayA[i] in tem:
                    if arrayB[i] in tem:
                        res.append(arrayC[i])
                    else:
                        res.append(arrayB[i])
                else:
                    res.append(arrayA[i])
            else:
                if arrayA[i]==res[i-1]:
                    res.append(arrayB[i])
                else:
                    res.append(arrayA[i])
        yield " ".join([str(x) for x in res])
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
