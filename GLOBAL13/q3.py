import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        arrs = list(map(int,input().split()))
        steps = 0
        while True:
            maxi = 0
            biggerThanOne = {}
            visited = {}
            for i,ele in enumerate(arrs):
                if arrs[ele] not in visited:
                    if ele>1:
                        biggerThanOne[i] = 1
                        maxi = max(maxi,1)
                        curr = i
                        vistied.add(i)
                        while True:
                            if curr + ele < n:
                                curr += ele
                                ele = arrs[curr]
                                if ele>1:
                                    biggerThanOne[i] += 1
                                    maxi = max(maxi,biggerThanOne[i])
                                    vistied.add(curr)
                                else:
                                    break
            if maxi==1:
        
                        

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
