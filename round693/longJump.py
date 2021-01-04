import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n = int(input())
        jumps = list(map(int,input().split()))
        dic = defaultdict(lambda:0)
        maxi = 0
        for index in range(n):
            kap = dic[index]+jumps[index]
            maxi= max(maxi,kap)
            dic[index+jumps[index]]=max(dic[index+jumps[index]],kap)
        yield maxi
                    
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
