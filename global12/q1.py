import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        arry = input()
        dic = {}
        for ele in arry:
            freq = dic.get(ele,0)
            dic[ele]=freq+1
        ans = []
        for i in range(26):
            curr = chr(ord('a')+i)
            freq = dic.get(curr,0)
            if freq:
                ans.extend([curr]*freq)
        yield ''.join([str(x) for x in ans])
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
