import sys
from bisect import bisect_left
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    return False


def gift():
    for _ in range(cou):
        n = int(input())
        lst= [int(x) for x in input().split()]

        newlst=lst[:]
        newlst.sort()

        less=0
        big=0

        onein=False
        bignotin=True
        error=False
        full=list(range(1,n*2+1))
        for ele in newlst:
            if ele<=n:
                less+=1
            else:
                big+=1
            if ele==1:
                onein=True
            if ele==n*2:
                bignotin=False
            full.remove(ele)
        #print(onein,bignotin,less<big,full)
        if onein and bignotin and less>=big:
            res=[]
            #print(lst,full)
            for ele in lst:
                #print(res)
                
                found=find_ge(full,ele)
                #print(found)
                if not found:
                    error=True
                    break
                res.append(ele)
                res.append(found)
                full.remove(found)
            if error:
                yield -1
            else:
                yield " ".join(str(x) for x in res)
            
        else:
            yield -1
       
            

            
            
        
        

if __name__ == '__main__':
    cou= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
