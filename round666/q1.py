import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        dic={}
        for i in range(n):
            currString = input()
            for char in currString:
                freq = dic.get(char,0)
                dic[char] = freq + 1
        ans = 'YES'
        for ele in dic:
            if dic[ele] % n !=0:
                ans = 'NO' 
                break
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
