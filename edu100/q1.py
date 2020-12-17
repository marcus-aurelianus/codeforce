import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        mos = list(map(int,input().split()))
        dingdong = sum(mos)%(len(mos)+6)
        kappa = sum(mos)//(len(mos)+6)
        if dingdong==0 and kappa<=min(mos):
            yield 'YES'
        else:
            yield 'NO'

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
