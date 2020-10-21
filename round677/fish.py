import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        fish = list(map(int,input().split()))
        maxFish = max(fish)
        if sum(fish)/n == maxFish:
            yield -1
        else:
            for i,ele in enumerate(fish):
                if ele == maxFish:
                    if i == 0:
                        if fish[i+1] == maxFish:
                            continue
                        else:
                            yield 1
                            break
                    elif i == n-1:
                        if fish[i-1] == maxFish:
                            continue
                        else:
                            yield n
                            break
                    else:
                        if fish[i-1]!=maxFish or fish[i+1]!=maxFish:
                            yield i+1
                            break

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
