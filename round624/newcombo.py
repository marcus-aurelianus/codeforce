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
        for i in range(26):
            dic[string[i]]=i
        dp=[[0]*26]
        for i in range(n):
            s=combo[i]
            pos=dic[s]
            if i==0:
                dp[0][pos]+=1
            else:
                temp=dp[-1][:]
                temp[pos]+=1
                dp.append(temp)
        res=[0]*26
        #print(dp)
        for i in range(p):
            arr=dp[plst[i]-1]
            #print(arr)
            res=[x + y for x, y in zip(arr, res)]
        for s in combo:
            res[dic[s]]+=1
        yield " ".join(map(str,res))
            

        

if __name__ == '__main__':
    cou= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
