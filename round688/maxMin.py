import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        nums = list(map(int,input().split()))
        B = []
        for i in range(n-1):
            B.append(abs(nums[i+1]-nums[i]))
        S2 = [0]
        for s in B:
            S2.append(S2[-1]+s)
        ans = min(sum(B[1:]),sum(B[:-1]))
        for i in range(n-2):
            ans = min(ans, S2[i]+(S2[-1]-S2[i+2])+abs(nums[i+2]-nums[i]))
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
