import sys
input = sys.stdin.readline
 
Q = int(input())
Query = [int(input()) for _ in range(Q)]
 
 
for N in Query:
    N -= 1
    seq = N//3
    where = N%3
    T = 0
    for l in range(100):
        a = 4**l
        if T + a > seq:
            start = (seq - T) + a
            break
        T += a
    if where == 0:
        print(start)
    else:
        b = start - a
        b_str = bin(b)[2:]
        b_str = "0"*(a.bit_length()-1 - len(b_str)) + b_str
        L = len(b_str)//2
        p_str = ""
        for l in range(L):
            tmp = b_str[2*l:2*l+2]
            if tmp == "00":
                p_str += "00"
            elif tmp == "01":
                p_str += "10"
            elif tmp == "10":
                p_str += "11"
            else:
                p_str += "01"
        second = int("10"+p_str, 2)
        if where == 1:
            print(second)
        else:
            print(start^second)
