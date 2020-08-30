import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        p, f = list(map(int,input().split()))
        c1, c2 = list(map(int,input().split()))
        w1, w2 = list(map(int,input().split()))

        if w1>w2:
            w1,w2=w2,w1
            c1,c2=c2,c1
        elif w1==w2:
            if c1<c2:
               c1,c2=c2,c1 

        len1 = min(p//w1,c1)

        ans = 0

        for i in range(len1+1):
            currans = i + min((p - w1*i)//w2,c2) + min((f//w1),(c1-i))+ min((f-min((f//w1),(c1-i))*w1)//w2,c2-min((p - w1*i)//w2,c2))
            
            ans = max(ans,currans)
        yield ans

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)





#3 2 3 3
