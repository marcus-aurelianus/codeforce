import random
def rts(string):
    n = len(string)
    left,q =0,0
    ans = True
    for i in range(n):
        if string[i]=='?':
            q+=1
        elif string[i]=='(':
            left+=1
        else:
            if left>0:
                left-=1
            elif q>0:
                q-=1
            else:
                ans = False
                break
    if ans and left==0:
        return True
    else:
        ans = True
        left,q =0,0
        for i in range(n):
            if string[n-1-i]=='?':
                q+=1
            elif string[n-1-i]==')':
                left+=1
            else:
                if left>0:
                    left-=1
                elif q>0:
                    q-=1
                else:
                    ans = False
                    break
        if ans and left==0:
            return True
        else:
            return False


def gift(string):
    n = len(string)
    if n%2:
        return False
    else:
        lans = True
        left,q =0,0
        for i in range(n):
            if string[i]=='?':
                if left==0:
                    left+=1
                else:
                    q+=1
            elif string[i]=='(':
                left+=1
            else:
                if left>0:
                    left-=1
                elif q>0:
                    q-=1
                else:
                    lans = False
                    break

        rans = True
        left,q =0,0
        for i in range(n):
            if string[n-1-i]=='?':
                if left==0:
                    left+=1
                else:
                    q+=1
            elif string[n-1-i]==')':
                left+=1
            else:
                if left>0:
                    left-=1
                elif q>0:
                    q-=1
                else:
                    rans = False
                    break
        if lans and rans:
            return True
        else:
            return False
for _ in range(1000):
    string=""
    for i in range(20):
        kap = random.randint(0, 1)
        if kap==0:
            string+='('
        else:
            string+=')'

    if rts(string):
        ranC = random.randint(1, 20)
        for fuc in range(ranC):
            pos = random.randint(0, 19)
            string=string[:pos]+"?"+string[pos+1:]
        if not gift(string):
            print(string)
        
            
