import sys

reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__




def gift():
    for _ in range(cou):

        n,p= [int(x) for x in input().split()]
        combo=input()
        plst=[int(x) for x in input().split()]
        string="abcdefghijklmnopqrstuvwxyz"
        dic={}
        for s in string:
            dic[s]=0

        dp=[0]*n
        for i in range(p):
            arr=[1]*plst[i]+[0]*(n-plst[i])
            #print(arr,dp)
            squares=[x + y for x, y in zip(arr, dp)]
            dp=squares
        #print(dp)
        for i in range(n):
            char=combo[i]
            #print(char,list(map(lambda x:x[i],dp)))
            freq=dp[i]
            currfreq=dic.get(char)
            dic[char]=freq+currfreq
        res=[]
        for s in combo:
            currfreq=dic.get(s)
            dic[s]=currfreq+1
        for key in dic:
            res.append(str(dic[key]))
        yield " ".join(res)
        

if __name__ == '__main__':
    cou= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
