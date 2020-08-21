import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry= list(map(int,input().split()))
        dic={}
        ans=[]
        for ele in arry:
            res=dic.get(ele,False)
            if not res:
                ans.append(ele)
            dic[ele]=True
        yield " ".join(str(x) for x in dic)
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
