import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
    
        
#print(len(inamo))
def gift():
    for _ in range(t):
        n=int(input())
        arry = list(map(int,input().split()))
        ans=[[0 for x in range(n)] for x in range(26)]
        for i in range(n):
            ans[arry[i]-1][i]=1

    
        for ele in ans:
            print (ele)
        yield ans
 
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
    

