import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
nn = "0123456789"
def gift():
    for _ in range(t):
        s=input()
        ans = len(s)
        for fi in nn:
            for sc in nn:
     
                state = 0
                now = 0
     
                for i in s:
                    if i == fi and state == 0:
                        now += 1
                        state = 1
                    elif i == sc and state == 1:
                        now += 1
                        state = 0
     
                if fi == sc:
                    ans = min(ans , len(s) - now)
                else:
                    ans = min(ans , len(s) - now + now%2)
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
             


#"{} {} {}".format(maxele,minele,minele)
