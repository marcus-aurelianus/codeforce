import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        s = sum(a)
        div = []
        i = 1
        while i**2 <= s:
     
            if i**2 == s:
                div.append(i)
            elif s % i == 0:
                div.append(i)
                div.append(s//i)
            i += 1
     
        div.sort()
        for d in div:
            L = s // d
            stk = 0
            for i in a:
                stk += i
                if stk == d:
                    stk = 0
                elif stk > d:
                    break
            else:
                yield (n-L)
                break

                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
    
# 5 1 2 4 5 1 6 4 2
