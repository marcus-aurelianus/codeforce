import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

string = input()

print(3)
print("L {}".format(len(string)-1))
print("R {}".format(len(string)-1))
print("R {}".format(2*len(string)-1))
            


#"{} {} {}".format(maxele,minele,minele)
# 0 1 1 0
# 1 0 1 1
# abcdefefe

# n
# 2n-2
# 3n-3-(n-2)
