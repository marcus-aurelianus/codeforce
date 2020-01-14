def angry():
    for _ in range(t):
        n = int(input())
        stus=input()
        res=0
        temp=None
        for i in range(n):
            if stus[i]=="A":
                if temp:
                    res=max(res,temp)
                temp=0
            else:
                if temp!=None:
                    temp+=1
                if i==n-1:
                    if temp==None:
                        temp=0

                    res=max(res,temp)
        yield res
if __name__ == '__main__':
    t= int(input())
    ans = angry()
    print(*ans,sep='\n')   
