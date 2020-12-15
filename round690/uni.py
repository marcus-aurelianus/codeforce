import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        if n>45:
            yield -1
        else:
            ans=[]
            curr=9
            while n>0:
                if n>=curr:
                    ans=[curr]+ans
                    n-=curr
                    curr-=1
                else:
                    ans=[n]+ans
                    n=0
            yield "".join([str(x) for x in ans])
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
    
