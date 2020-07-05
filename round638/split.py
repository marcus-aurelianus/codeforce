def go(n, c, g, k):
    if k:
        t = min(c, (n - g - k * c) / k)
        a.append(t)
        go(n, c + t, g + c + t, k - 1)
 
T = int(input())
for _ in range(T):
    n = int(input())
    k = n.bit_length() - 1
    print (k)
    a = []
    go(n, 1, 1, k)
    for x in a:
        print (x),
    print
