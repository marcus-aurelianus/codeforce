import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n, k = list(map(int,input().split()))
        arry = list(input())
        if n%k:
            lent = n//k+1
        else:
            lent = n//k
        ans = True
        for j in range(k):

            curr = None
            for i in range(lent):
                now = i*k + j
                #print(i,j,now)
                if now<= n-1:
                    if arry[now]!='?':
                        if not curr:
                            curr = arry[now]
                            break
            if curr:
                for i in range(lent):
                    now = i*k + j
                    #print(i,j,now)
                    if now<= n-1:
                        if arry[now]=='?':
                            arry[now]=curr
                        elif arry[now]!='?' and curr != arry[now]:
                            ans=False
                            break
            if not ans:
                break
        count1 = 0
        count0 = 0
        other = 0
        #print(arry)
        for i in range(k):
            if arry[i] == '0':
                count0 += 1
            elif arry[i] == '1':
                count1 += 1
            else:
                other += 1
        if count0 != count1 and min(count0,count1)+other<max(count0,count1):
            ans = False
        
        yield 'YES' if ans else 'NO'            
                    
                
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
