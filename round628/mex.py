
  
import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__



if __name__ == '__main__':
    n= int(input())
    arr=[]
    for i in range(n):
        a1,a2=list(map(int,input().split()))
        arr.append([a1,a2,a1+a2])
        
#mex(1,6)=2
#mex(1,3)=0
#mex(1,4)=1
