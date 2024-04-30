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


## approach having time complexity nlogn
def binarySearch(start, end, i, k, arr):
    mid = (start + end) // 2

    if i+k == arr[mid]:
        return [i,arr[mid]]
    
    if arr[mid] < i+k:
        binarySearch(0, mid, i, k, arr)
    else:
        binarySearch(mid, len(arr), i, k, arr)

    return -1

def secondApproachcountNumberOfPairsHavingDifferenceK(arrlist, k):
    sortedarrlist = sorted(arrlist)
    for i in range(arrlist[i]):
        binarySearch(0, len(arrlist), arrlist[i], k, arrlist)
    

arrlist = [1,7,5,9,2,12,3]
k=2
getpair = secondApproachcountNumberOfPairsHavingDifferenceK(arrlist, k)
print(getpair)