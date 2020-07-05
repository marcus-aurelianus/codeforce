import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

n,s = list(map(int,input().split()))
if s<=2*n-1:
    print('NO')
else:
    Ans = [1] * (n - 1)
    Ans.append(s - n + 1)
    print("YES")
    print(" ".join(map(str, Ans)))
    print(n)
  
            
