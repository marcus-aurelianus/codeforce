import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        nums = input()
        got = False
        if n%2:
            
            for i in range(n//2+1):
                if int(nums[i*2])%2:
                    got = True
                    break
            if not got:
                ans = 2
            else:
                ans = 1
        else:
            for i in range(n//2):
                if int(nums[i*2+1])%2 == 0:
                    got = True
                    break
            if not got:
                ans = 1
            else:
                ans = 2
        yield ans
                        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
