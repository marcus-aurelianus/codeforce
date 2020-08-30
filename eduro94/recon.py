import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
 
def gift():
    for _ in range(t):
        string = input()
        x = int(input())
        n = len(string)
 
        markpoint=[]
        Failed=False
        for i in range(n):
            if string[i] == '0':
                markpoint.append(i)
 
        dic={}
        for ele in markpoint:
            if ele-x>=0:
                dic[ele-x]=True
            if ele+x<=n-1:
                dic[ele+x]=True
        #print(dic)
        for ele in dic:
            if ele-x>=0:
                if ele-2*x>=0:
                    if dic.get(ele-2*x,False):
                        if string[ele-x]!='0':
                            Failed=True
                            break
                    else:
                         if string[ele-x]!='1':
                            Failed=True
                            break                       
                else:
                    if string[ele-x]!='0':
                        Failed=True
                        break
            
            if ele+x<=n-1:
                if ele+2*x<=n-1:
                    if dic.get(ele+2*x,False):
                        if string[ele+x]!='0':
                            Failed=True
                            break
                    else:
                         if string[ele+x]!='1':
                            Failed=True
                            break 
                else:
                    if string[ele+x]!='0':
                        Failed=True
                        break
        if Failed:
            yield -1
        else:
            ans = []
            for i in range(n):
                if dic.get(i,False):
                    ans.append('0')
                else:
                    ans.append('1')
            kap=''.join(ans)
            right=True
            for i in range(n):
                curr=False
                if i-x>=0:
                    if kap[i-x]=='1':
                        curr=True
                if i+x<=n-1:
                    if kap[i+x]=='1':
                        curr=True
                if curr:
                    if string[i]!='1':
                        right=False
                        break
                else:
                    if string[i]!='0':
                        right=False
                        break
            if right:
                yield kap
            else:
                yield -1
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
 
 
#"{} {} {}".format(maxele,minele,minele)
