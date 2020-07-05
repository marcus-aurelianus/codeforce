import sys
input = sys.stdin.buffer.readline
 
#import io, os
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
ans1 = 0
ans2 = 0
for i, num in enumerate(a):
    if num % p != 0:
        ans1 = i
        break
for i, num in enumerate(b):
    if num % p != 0:
        ans2 = i
        break
print(ans1 + ans2)
