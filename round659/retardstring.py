import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):

        n = int(input())
        string1 = input()
        string2 = input()

        ans=True

        for i in range(n):
            if ord(string1[i])>ord(string2[i]):
                ans=False
                break

        if ans:
            if string1[0]!=string2[0]:
                count1,count2=1,1
            else:
                count1,count2=0,0

            curmin=string1[i]
            for i in range(n-1):
                if string1[i+1]!=string2[i+1]:
                    if string1[i]!=string1[i+1]:
                        count1+=1
                    if string2[i]!=string2[i+1]:
                        count2+=1
            yield max(count1,count2)

        else:
            yield -1
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# aabaac
# bbccdd
