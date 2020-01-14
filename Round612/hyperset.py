

n ,m = map(int,(input().split()))
cards={}
cardsL=[]
ans={}
for i in range(n):
    card=input()
    cards[card]=i
    cardsL.append(card)

def getCard3(A,B,m):
    card3=""
    for i in range(m):
        if A[i]==B[i]:
            card3+=A[i]
        elif A[i]!="T" and B[i]!="T":
            card3+="T"
        elif A[i]!="E" and B[i]!="E":
            card3+="E"
        elif A[i]!="S" and B[i]!="S":
            card3+="S"
    return card3
res=0
for i in range(n-1):
    for j in range(i+1,n-1):
        CardT=getCard3(cardsL[i],cardsL[j],m)
        temp=cards.get(CardT,0)
        if temp>j:
            res+=1       
print(res)



