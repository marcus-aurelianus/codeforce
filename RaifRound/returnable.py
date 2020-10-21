import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        belt = input()
        #a,b,c,d= list(map(int,input().split()))
        tr = 0
        tl = 0
        ans = 0
        cl = 0
        cr = 0
        for i in range(n):
            l , r = belt[i],belt[(i-1)%n]
            if l == '-' or r =='-':
                ans += 1
            else:
                if r == '>':
                    tr += 1
                if l == '<':
                    tl += 1
            if l == '>':
                cr += 1
            if l == '<':
                cl += 1
        #print(ans,tl,tr)
        if tr>0 and cl==0:
            ans += tr
        elif cr==0 and tl>0:
            ans+=tl
        yield ans

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
