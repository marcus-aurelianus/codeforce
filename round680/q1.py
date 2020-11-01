import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        
        n,x = list(map(int,input().split()))
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))

        if _ <t-1:
            c = input()
        a.sort()
        b.sort(reverse=True)
        ans = True
        for i in range(n):
            if a[i]+b[i]>x:
                ans=False
                break
        if ans:
            yield 'YES'
        else:
            yield 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
