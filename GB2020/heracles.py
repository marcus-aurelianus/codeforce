import sys
input = sys.stdin.buffer.readline
from collections import defaultdict

def gift():
    for _ in range(t):
        n = int(input())
        nodes = list(map(int,input().split()))
        dic = defaultdict(lambda:[])
        for i in range(n-1):
            k,v = list(map(int,input().split()))
            dic[k].append(v)
            dic[v].append(k)

        ans = [sum(nodes)]

        dingdong = []
        for key in dic:
            if len(dic[key])>1:
                dingdong.append([nodes[key-1],len(dic[key])-1])

        dingdong.sort(key=lambda x:-x[0])

        currIndex = 0
        
        for i in range(n-2):
            currItem = dingdong[currIndex]
            toA,freq = currItem
            ans.append(ans[-1]+toA)
            currItem[1]-=1
            if currItem[1]==0:
                currIndex+=1
                
        yield " ".join([str(x) for x in ans])  

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
# baebdcb
