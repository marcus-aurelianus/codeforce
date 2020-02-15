import sys

reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def keyboard():
    for _ in range(t):
        string=input()
        strcoll=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        res=[]
        res+=[string[0]]
        strcoll.remove(string[0])
        n=len(string)
        currpos=1


        resok=True
        if n==1:
            resok=True
        else:
            if string[1]==res[0]:
                resok=False

            else:
                res+=string[1]
                
                strcoll.remove(string[1])
                for i in range(n-2):
                    #print(currpos,res)
                    currlen=len(res)
                    if currpos==0:
                        if res[currpos+1]==string[i+2]:
                            currpos+=1
                        else:
                            if string[i+2] in strcoll:
                                res=[string[i+2]]+res
                                strcoll.remove(string[i+2])
                                currpos=0
                            else:
                                resok=False
                                break
                    elif currpos+1==currlen:
                        if res[currpos-1]==string[i+2]:
                            currpos-=1
                        else:
                            if string[i+2] in strcoll:
                                res=res+[string[i+2]]
                                strcoll.remove(string[i+2])
                                currpos+=1
                            else:
                                resok=False
                                break
                    else:
                        if res[currpos+1]==string[i+2]:
                            currpos+=1
                        elif res[currpos-1]==string[i+2]:
                            currpos-=1
                        else:
                            resok=False
                            break
        result=res+strcoll
        if resok:
            yield 'YES'
            yield "".join(result)
        else:
            yield 'NO'
        
if __name__ == '__main__':
    t= int(input())
    ans = keyboard()
    print(*ans,sep='\n')
            
