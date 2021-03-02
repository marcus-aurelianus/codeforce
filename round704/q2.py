import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        eles = list(map(int,input().split()))
        tmp = [True] * n
        target = n - 1
        end = n
        i = n - 1
        ans = []
        while True:
            if eles[i] != target + 1:
                i -= 1
            else:
                for j in range(i,end):
                    tmp[eles[j]-1] = False
                    ans.append(eles[j])
                end = i
                while not tmp[target] and target>=0:
                    target -= 1
            if target==-1:
                break
            #print(target,i)
        yield ' '.join([str(x) for x in ans])
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
