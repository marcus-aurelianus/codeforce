import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        arry = list(map(int,input().split()))
        count0 = 0
        count1 = 0
        for i in range(n):
            if arry[i] == 1:
                count1 += 1
            else:
                count0 += 1
        if count0>count1:
            if count0%2:
                count0-=1
            yield count0
            yield " ".join(str(x) for x in count0*[0])
        elif count0<count1:
            if count1%2:
                count1-=1
            yield count1
            yield " ".join(str(x) for x in count1*[1])
        else:
            yield count0
            yield " ".join(str(x) for x in count0*[0])            

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
#1 0 1 0 1 0
