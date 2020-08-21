import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        dic={}
        for ele in a:
            dic[ele]=True
        found=False
        for ele in b:
            if dic.get(ele,False):
                yield 'YES'
                yield "1 {}".format(ele)
                found=True
                break
        if not found:
            yield 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
