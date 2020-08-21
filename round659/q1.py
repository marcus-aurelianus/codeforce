import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import copy

def gift():
    for _ in range(t):

        n=input()
        arry = list(map(int,input().split()))


        ans=[]

        maxlen=max(arry)
        ans.append(['a']*(maxlen+1))

        for i,ele in enumerate(arry):
            lastele=ans[-1]
            temp=copy.deepcopy(lastele)
            #print(temp)
            temp[ele]=chr((ord(temp[ele])+1-ord('a'))%26+ord('a'))
            ans.append(temp)
        for ina in ans:
            yield "".join(ina)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
