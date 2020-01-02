import copy
if __name__ == '__main__':
    N = int(input())
     
    a = list(map(int,input().split()))
     
    end = [False] * N
    give = []
     
    for i in range(N):
     
        if a[i] != 0:
            end[a[i] - 1] = True
     
        else:
            give.append(i)
     
    want = []
     
    for i in range(N):
        if not end[i]:
            want.append(i)
     
    for i in range(len(give) - 1):
     
        if give[i] == want[i]:
            t = want[i+1]
            want[i+1] = want[i]
            want[i] = t
     
    if give[-1] == want[-1]:
        t = want[-1]
        want[-1] = want[-2]
        want[-2] = t
     
    for i in range(len(give)):
     
        a[give[i]] = want[i] + 1  
    print(" ".join(str(x) for x in a))
    
    

