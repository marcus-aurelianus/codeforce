import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def substr():
    for _ in range(t):
        strfrom=input()
        strto=input()
        start=0
        n=len(strto)
        res=1
        tempstart=0
        find=True
        while start<n:
            
            chartofind=strto[start]
            
            idx=strfrom.find(chartofind,tempstart)
            #print(strfrom,chartofind)
            #print(idx)
            if idx==-1:
                if tempstart==0:
                    find=False
                    break
                else:
                    tempstart=0
                    res+=1
            else:
                start+=1
                tempstart=idx+1
        if not find:
            yield -1
        else:
            yield res


if __name__ == '__main__':
    t= int(input())
    ans = substr()
    print(*ans,sep='\n')
