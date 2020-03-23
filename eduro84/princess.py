import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        chosen=list(range(1,n+1))
        dic={}
        #print(n)
        for i in chosen:
            dic[i]=False
        count=0
        queenwithnohusand=None
        lstrino=[]
        for i in range(n):
            lst = list(map(int,input().split()))
            lstrino.append(lst)
        for i in range(n):
            lst=lstrino[i]
            princesschoice=lst[1:]
            found=False
            for ele in princesschoice:       
                if not dic[ele]:
                    dic[ele]=True
                    count+=1
                    found=True
                    break
            if not found and not queenwithnohusand:
                queenwithnohusand=i+1

                
        for ele in dic:
            if not dic[ele]:
                #print(ele,dic)
                husbandcouldbe=ele
                break

        #print(dic)
        if count==n:
            yield 'OPTIMAL'
        else:
            yield 'IMPROVE'
            yield str(queenwithnohusand)+" "+str(husbandcouldbe)

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
