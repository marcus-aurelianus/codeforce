import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

sys.setrecursionlimit(300000)



def gift():
    def dfs(v,pa):
        good = 0
        bad = 0
        for nex in dic[v]:
            if nex != pa:
                nans,ng,nb = dfs(nex,v)
                if not nans:
                    return nans,0,0
                good += ng
                bad  += nb
     
        num = good + bad + p[v]
        if (num - h[v]) % 2 == 0:
            newbad  = (num - h[v])//2
        else:
            return False,0,0
        newgood = num - newbad
     
        if newbad - p[v] > bad or newgood < good or newbad < 0 or newgood < 0:
            return False,0,0
        else:
            return True,newgood,newbad
    for _ in range(t):
        city,people = list(map(int,input().split()))
        p = list(map(int,input().split()))
        h = list(map(int,input().split()))

        dic = [ [] for i in range(city)]
        for i in range(city-1):
            s,e = list(map(int,input().split()))
            dic[s-1].append(e-1)
            dic[e-1].append(s-1)
            
        ans,good,bad=dfs(0,0)
                 
        yield 'YES' if ans else 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
