import sys
input = sys.stdin.readline
 
def check(x):
    S=str(x)
    for s in S:
        if s!="0":
            if x%int(s)!=0:
                return 0
 
    return 1
        
    
 
t=int(input())
for tests in range(t):
    n=int(input())
    for x in range(n,10**19):
        if check(x)==1:
            print(x)
            break
        
import sys
input = sys.stdin.readline
 
def check(x):
    S=str(x)
    for s in S:
        if s>"1":
            if x%int(s)!=0:
                return 0
 
    return 1
 
t=int(input())
for tests in range(t):
    n=int(input())
    for x in range(n,10**19):
        if check(x)==1:
            print(x)
            break
