import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n, x = list(map(int,input().split()))
        array = list(map(int,input().split()))

        start = 0
        ans = 0
        lastend = 0
        while start<n-1:
            if array[start]<=array[start+1]:
                start+=1
            else:
                end = start
                gotAns=False
                while end>=lastend:
                    if array[end]>x and x<=array[start+1] and ((end>0 and x>=array[end-1]) or (end==0)):
                        gotAns = True
                        x,array[end] = array[end],x
                        ans += 1
                        break
                    else:
                        end-=1
                if not gotAns:
                    ans = -1
                    break
        yield ans
                        
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
