import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        charit=input()
        n=len(charit)
        count0,count1=0,0
        for ele in charit:
            if ele=="0":
                count0+=1
            else:
                count1+=1
        dud=min(count0,count1)
        if dud%2:
            yield 'DA'
        else:
            yield 'NET'

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
