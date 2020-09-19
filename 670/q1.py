import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict

def gift():
    for _ in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        array.sort()
        dic=defaultdict(lambda:0)
        for ele in array:
            dic[ele]+=1
        counter=0
        ans=0
        for i in range(102):
            if counter==0:
                if dic[i]==1:
                    ans+=i
                    counter+=1
                elif dic[i]==0:
                    ans+=2*i
                    counter+=2
            elif counter==1:
                if dic[i]==0:
                    ans+=i
                    break
            else:
                break
        yield ans
                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
