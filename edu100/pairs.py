import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input()) 

        b = list(map(int,input().split()))
        b.append(2*n+1)

        rem = []
        nex = 1
        for i in b:
            while nex != i:
                rem.append(nex)
                nex += 1
            nex += 1

        l = 0
        r = n+1

        while r-1!=l:

            m = (l+r)//2
            flag = True
            for i in range(m):
                if b[m-1-i]>rem[n-1-i]:
                    flag = False
                    break
            if flag:
                l = m
            else:
                r = m
        maxx = l
        l = 0
        r = n+1
        while r-l != 1:
            m = (l+r)//2
            flag = True
     
            for i in range(m):
                if rem[m-1-i] >= b[n-1-i]:
                    flag = False
                    break
            if flag:
                l = m
            else:
                r = m
        minx = n-l

        yield maxx-minx+1
                        

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 3 17
# 17 1
