import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


if __name__ == '__main__':
    n,mod = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    ans=1
    nums.sort()
    diff=dict()

        
    print(ans)
