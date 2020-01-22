import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def pack():
    for _ in range(t):
        n=int(input())
        lst=[]
        for i in range (n):
            lst.append(list(map(int,input().split())))
        lst.sort(key=lambda x:(x[0],x[1]))
        res=""
        prev=[]
        yn='YES'
        for i in range(n):
            if i==0:
                res+=lst[i][0]*"R"+lst[i][1]*"U"
            else:
                curr=lst[i]
                if curr[0]>=prev[0] and curr[1]<prev[1]:
                    yn='NO'
                    break
                else:
                    res+=(curr[0]-prev[0])*"R"+(curr[1]-prev[1])*"U"
            prev=lst[i]
        if yn=="YES":
            yield yn
            yield res
        else:
            yield yn

if __name__ == '__main__':
    t= int(input())
    ans = pack()
    print(*ans,sep='\n')
