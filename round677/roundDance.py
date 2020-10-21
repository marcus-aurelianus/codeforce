import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math

n = int(input())

print(math.factorial(n)//math.factorial(n//2)//n*math.factorial(n//2-1))
