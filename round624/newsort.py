import sys

reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def checkmonotone(lst):
    lenl=len(lst)
    if lenl==1:
        return True
    else:
        for i in range(lenl-1):
            if lst[i]>lst[i+1]:
                return False
        return True


def gift():
    for _ in range(cou):

        n,p= [int(x) for x in input().split()]
        nlst=[int(x) for x in input().split()]
        plst=[int(x) for x in input().split()]

        plst.sort()

        ranges=[[plst[0],plst[0]+1]]
        #print(plst)
        for i in range(p-1):
            currplst=plst[i+1]
            #print(currplst)
            if currplst==ranges[-1][-1]:
                rstart,rend=ranges.pop()
                ranges.append([rstart,currplst+1])
            else:
                ranges.append([currplst,currplst+1])
        #print(ranges)
        res=[]

        if ranges[0][0]!=1:
            tosorts,tosorte=0,ranges[0][0]-1
            templst=nlst[tosorts:tosorte]
            res+=templst
        #print(res,nlst,ranges)   
        rangen=len(ranges)
        for i in range(rangen):
            currs,curre=ranges[i][0]-1,ranges[i][1]
            blanks,blanke=False,False
            if i!=rangen-1:
                
                blanks,blanke=ranges[i][1],ranges[i+1][0]-1
            else:
                if ranges[-1][1]!=n:
                    blanks,blanke=ranges[-1][1],n
            
            templst=nlst[currs:curre]
            
            templst.sort()
            #print(templst,templst1,"temp",blanks,blanke)
            res+=templst
            if blanks:
                templst1=nlst[blanks:blanke]    
                res+=templst1
        #print(res,nlst,ranges,'res')
        if checkmonotone(res):
            yield 'YES'
        else:
            yield 'NO'

        

if __name__ == '__main__':
    cou= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
