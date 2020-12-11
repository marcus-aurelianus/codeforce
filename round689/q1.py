import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        ans = ['a']*k + (n-k)//3*['bca']
        if (n-k)%3==2:
            ans.append('bc')
        elif (n-k)%3==1:
            ans.append('b')
        yield "".join(ans)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
