import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def maxSubArraySum(a,size): 
       
    max_so_far = -(float("inf"))
    max_ending_here = 0
       
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max_so_far 
def gift():
    for _ in range(t):
        n=int(input())
        arry=list(map(int,input().split()))

        sum1=0
        for i in range(n//2+n%2):
            sum1+=arry[2*i]


        arra=[]
        arrb=[]
        for i in range(n//2):
            arra.append(arry[2*i+1]-arry[2*i])
        for i in range(n//2-1+n%2):
            arrb.append(arry[2*i+1]-arry[2*(i+1)])
        diua=maxSubArraySum(arra,len(arra))
        diub=maxSubArraySum(arrb,len(arrb))
        
        yield sum1+max(diua,diub,0)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
