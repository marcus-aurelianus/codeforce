import sys

reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def checkmonotone(lst):
    n=len(lst)
    if n==1:
        return True
    else:
        for i in range(n-1):
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
        for i in range(p-1):
            currplst=plst[i+1]
            if currplst==ranges[-1][-1] or currplst==ranges[-1][-1]+1:
                rstart,rend=ranges.pop()
                ranges.append([rstart,currplst+1])
            else:
                ranges.append([currplst,currplst+1])
        if ranges==[]:
            if checkmonotone(nlst):
                yield 'YES'
            else:
                yield 'NO'
        elif ranges[0][0]==1:
            rangen=len(ranges)
            if rangen==1:
                e=ranges[0][1]
                if e==n:
                    yield 'YES'
                else:
                    if max(nlst[0:e])<=nlst[e]) and checklst(nlst[e:]):
                        yield 'YES'
                    else:
                        yield 'NO'
            else:
                correct=True
                for i in rangen:
                    blanks,blanke=ranges[i][1],ranges[i+1][0]

                    prevs,preve=ranges[i][0],ranges[i][1]
                    nexts,nexte=ranges[i+1][0],ranges[i+1][1]
                    if checklst(nlst[blanks:blanke]) and max(nlst[ranges[i][0]:ranges[i][1]])<=nlst[preve] and min(nlst[ranges[i+1][0]:ranges[i+1][1]])>=nlst[ranges[i+1][0]-1]:
                        continue
                    else:
                        correct=False
                        break
                s,e=ranges[-1]
                if e!=n:
                    if max(nlst[s:e])>nlst[e]) or not checklst(nlst[e:]):
                        correct=False
                if correcnt:
                    yield 'YES'
                else:
                    yield 'NO'
                    
        else:
            excludedranges=[[1,ranges[0][0]]]

            
                   
        
        yield ranges
    
        

if __name__ == '__main__':
    cou= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
