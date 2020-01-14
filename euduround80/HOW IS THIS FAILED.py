n ,m = map(int,(input().split()))
cards={}
cardsL=[]
ans={}
for i in range(n):
    card=input()
    cards[card]=i
    cardsL.append(card)
 
def getCard3(A,B,m):
    dict1={("S","E"):"T",("S","T"):"E",("T","E"):"S",("T","S"):"E",("E","S"):"T",("E","T"):"S"}
    card3=""
    for i in range(m):
        if A[i]==B[i]:
            card3+=A[i]
        else:
            tempstr=dict1[(A[i],B[i])]
            card3+=tempstr
    return card3
res=0
for i in range(n-1):
    for j in range(i+1,n-1):
        CardT=getCard3(cardsL[i],cardsL[j],m)
        temp=cards.get(CardT,0)
        if temp>j:
            res+=1       
print(res)
