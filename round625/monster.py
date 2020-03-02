import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


if __name__ == '__main__':

    n,m,p = [int(x) for x in input().split()]
    weapon=[]
    weaponprice=[]
    armor=[]
    armorprice=[]
    monster=[]
    unsortedweapon=[]
    unsortedarmor=[]
    for i in range(n):
        newweapon=[int(x) for x in input().split()]
        unsortedweapon.append(newweapon)
    unsortedweapon.sort(key=lambda x:x[0])
    for weaponrino in unsortedweapon:
        newW,newWP=weaponrino
        weapon.append(newW)
        weaponprice.append(newWP)
    for i in range(m):
        newarmor=[int(x) for x in input().split()]
        unsortedarmor.append(newarmor)
    unsortedarmor.sort(key=lambda x:x[0])
    for armorino in unsortedarmor:
        newA,newAP=armorino
        armor.append(newA)
        armorprice.append(newAP)
    for i in range(p):
        newM=[int(x) for x in input().split()]
        monster.append(newM)
    
    monster.sort(key=lambda x:x[0])
    print(unsortedweapon)
    print(unsortedarmor)
    print(monster)
    currWi,currAi=weaponprice.index(min(weaponprice)),armorprice.index(min(armorprice))
    currW,currA=weapon[currWi],armor[currAi]
    #print(armorprice,currAi)
    currProfit=0
    for i in range(p):
        #print(i,currAi,currWi)
        if monster[i][0]<currW and monster[i][1]<currA:
            currProfit+=monster[i][2]
        else:
            profitGain=monster[i][2]
            dmg,defense=False,False
            if monster[i][0]>=currW:
                if currWi<n-i:
                    dmg=weapon[currWi+1]
                    costW=weaponprice[currWi+1]
            if monster[i][1]>=currA:
                if currAi<n-i:
                    defense=armor[currAi+1]
                    costA=armorprice[currAi+1]
            #print(dmg,defense,monster[i])
            if dmg>monster[i][0] and defense>monster[i][1]:
                if costW<=costA and (costW-weaponprice[currWi])<profitGain:
                    currProfit+=(monster[i][2])
                    currWi+=1
                    currW=dmg
                elif costW>=costA and (costA-armorprice[currAi])<profitGain:
                    currProfit+=(monster[i][2])
                    currAi+=1
                    currA=defense
                else:
                    continue
            elif dmg>monster[i][0]:
                if (costW-weaponprice[currWi])<profitGain:
                    currProfit+=(monster[i][2])
                    currWi+=1
                    currW=dmg
                else:
                    continue
            elif defense>monster[i][1]:
                if (costA-armorprice[currAi])<profitGain:
                    currProfit+=(monster[i][2])
                    currAi+=1
                    currA=defense
                else:
                    continue
            else:
                continue
    #print(currProfit,currWi,currAi)
    print(currProfit-weaponprice[currWi]-armorprice[currAi])
                    
            
