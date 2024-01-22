## First approach having n square approach

def firstApproachcountNumberOfPairsHavingDifferenceK(arrlist):
    if len(arrlist) == 0 or len(arrlist)==1:
        return "No Element match"
    
    pairlist = []
    for i in range(len(arrlist)):
        for j in range(i+1, len(arrlist)):
            diff = arrlist[i] - arrlist[j]
            if abs(diff) == 2:
                pairlist.append([arrlist[i], arrlist[j]])

    return pairlist


## wrong approach
def secondApproachcountNumberOfPairsHavingDifferenceK(arrlist):
    sortedarrlist = sorted(arrlist)
    print("sortedarrlist",sortedarrlist)
    pairlist = []
    for i in range(len(sortedarrlist)-1):
        if abs(sortedarrlist[i] - sortedarrlist[i+1])==2:
            pairlist.append([sortedarrlist[i], sortedarrlist[i+1]])

    return pairlist

arrlist = [1,7,5,9,2,12,3]
getpair = secondApproachcountNumberOfPairsHavingDifferenceK(arrlist)
print(getpair)