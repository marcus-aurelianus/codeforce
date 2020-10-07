import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        array = list(map(int,input().split()))
        minItem = min(array)
        met = False
        minRes = 0
        for i in range(n):
            if array[i] == minItem:
                if met == False:
                    met = True
                    continue
            minRes += (k-array[i])//minItem


        yield minRes
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
