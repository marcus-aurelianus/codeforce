import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        string=input()
        n=len(string)
        ans=[]
        for i in range(n):
            if i==0 or i==n-1:
                ans.append(string[i])
            elif i%2:
                ans.append(string[i])
        yield "".join(str(x) for x in ans)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
