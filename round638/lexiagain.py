import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        word=list(input())
        word.sort()
        #print(word)
        if k==1:
            yield "".join(str(x) for x in word)
        elif n==k:
            yield word[n-1]
        else:
            cur=word[k-1]
            if cur!=word[0]:
                yield cur
            else:
                nextele=word[k]
                nexrep=True
                for i in range(k+1,n):
                    if word[i]!=nextele:
                        nexrep=False
                        break
                if (n-k)%k==0:
                    end=k+(n-k)//(k)
                else:
                    end=k+(n-k)//(k)+1
                if nexrep:
                    yield "".join(str(x) for x in word[k-1:end])
                else:
                    yield "".join(str(x) for x in word[k-1:])
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
