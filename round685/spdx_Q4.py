import sys
from sys import stdin
 
def solve(aAB,aBC,aCA,oAB,oBC):
 
    ans = []
 
    for A in range(2):
        for B in range(2):
            for C in range(2):
 
                if A&B==aAB and B&C==aBC and C&A==aCA and A|B==oAB and B|C==oBC: # and C|A==oCA:
                    return A,B,C
 
    return None,None,None
 
n = int(stdin.readline())
ans = [0] * n
 
print ("AND",1,2,flush=True)
aAB = int(stdin.readline())
print ("AND",2,3,flush=True)
aBC = int(stdin.readline())
print ("AND",3,1,flush=True)
aCA = int(stdin.readline())
 
print ("OR",1,2,flush=True)
oAB = int(stdin.readline())
print ("OR",2,3,flush=True)
oBC = int(stdin.readline())
#print ("OR",3,1,flush=True)
#oCA = int(stdin.readline())
 
for i in range(17):
    m = 2**i
    t0,t1,t2 = solve( ((aAB&m)>>i),((aBC&m)>>i),((aCA&m)>>i),((oAB&m)>>i),((oBC&m)>>i))
    ans[0] |= t0*m
    ans[1] |= t1*m
    ans[2] |= t2*m
 
#print (ans[:3],file=sys.stderr)
 
for i in range(4,n+1):
    print ("XOR",1,i,flush=True)
    ans[i-1] = ans[0] ^ int(stdin.readline())
 
print ("!",*ans,flush=True)
