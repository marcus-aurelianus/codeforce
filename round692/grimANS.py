import sys
readline = sys.stdin.readline
 
S = [1 if s == '1' else 0 if s == '0' else -1 for s in readline().strip()]
zo, oz = map(int, readline().split())
 
if zo > oz:
    zo, oz = oz, zo
    S = [[1, 0, -1][s] for s in S]
 
def calc(m):
    res = 0
    zero = 0
    one = 0
    cnt = 0
    for s in S:
        if s == -1:
            cnt += 1
            if cnt <= m:
                res += oz*one
                zero += 1
            else:
                res += zo*zero
                one += 1
        elif s == 0:
            res += oz*one
            zero += 1
        else:
            res += zo*zero
            one += 1
    return res
 
l = 0
r = S.count(-1)
 
while abs(r-l) > 2:
    m1 = (2*l+r)//3
    m2 = (l+2*r)//3
    if calc(m1) < calc(m2):
        r = m2
    else:
        l = m1
 
print(min(calc(k) for k in range(l, r+1)))
