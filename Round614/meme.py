def checkN(string):
    for ele in string:
        if ele!='9':
            return False
    return True
def meme():
    for _ in range(t):
        a,b = [int(x) for x in input().split()]


        strb=str(b)
        
        if checkN(strb):
            res1=a*(len(str(b)))
        else:
            res1=a*(len(str(b))-1)
        yield res1

                    

if __name__ == '__main__':
    t= int(input())
    ans = meme()
    print(*ans,sep='\n')
