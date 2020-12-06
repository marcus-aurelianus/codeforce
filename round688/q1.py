import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        a1 = list(map(int,input().split()))
        a2 = list(map(int,input().split()))
        dic = {}
        for ele in a1:
            dic[ele]=True
        ans = 0
        for ele in a2:
            if dic.get(ele,False):
                ans+=1
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
