import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        num=int(input())
        if num<=3:
            yield -1
        else:
            ans=list(map(lambda x:x*2,range(1,num//2+1)))
            ans.append(num//2*2-3)
            for i in range(num//2+num%2,0,-1):
                if i*2-1!=num//2*2-3:
                    ans.append(i*2-1)
            yield " ".join(str(x) for x in ans)
        
                
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')



##2 4 6 8 10 12 9 11 7 5 3 1
##2 4 1 3
