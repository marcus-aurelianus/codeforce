import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n=int(input())
        array = list(map(int,input().split()))
        if n==1:
            yield array[0]
        elif n==2:
            if array[0]==array[1]:
                yield " ".join(str(x) for x in array)
            else:
                yield "-1 "+str(min(array))
        else:
            dic = defaultdict(lambda:[])

            for i in range(n):
                dic[array[i]].append(i)

            ans = [0]*n
            minmaxLen = float("inf")
            minMaxVal = None
            for ele in dic:
                curr = dic[ele]
                maxLen = curr[0]+1
                for i in range(len(curr)):
                    if i==len(curr)-1:
                        #print(curr,n)
                        maxLen = max(n - curr[i],maxLen)
                    else:
                        maxLen = max(curr[i+1] - curr[i],maxLen)
                if maxLen<minmaxLen:
                    minMaxVal = ele
                    minmaxLen = maxLen


            for i in range(min(n//2,minmaxLen-1)):
                ans[i] = -1

            for i in range(minmaxLen-1,n//2):
                ans[i] = minMaxVal

            currMin = minMaxVal
            for j in range(n//2,n):
             
                i = j-n//2
                if n%2:

                    if i==0:
                        currMin = max(min(array[:n//2]),min(array[n//2:]))
                    else:
                        currMin = min(currMin,array[n//2+i],array[n//2-i])
                else:
                    if i==0:
                        currMin = max(min(array[:n//2]),min(array[n//2:]))
                    else:
                        currMin=min(currMin,array[n//2+i],array[n//2-1-i])
                #print(j,currMin)
                ans[j] = currMin
            yield " ".join(str(x) for x in ans)
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
