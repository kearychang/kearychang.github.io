def binarySearchIndexMinimizeDiff(arr, target):
    if len(arr) == 0:
        return
    else:
        startIndex = 0
        endIndex = len(arr)-1
        midIndex = 0
        while (endIndex - startIndex) >= 1:
            midIndex = (startIndex + endIndex)//2
            if arr[midIndex] <= target:
                startIndex = midIndex+1
            else:
                endIndex = midIndex
        return endIndex

def advantageCount(A,B):
    #sort A, create Bsorted
    A.sort()
    tmpA = A[:]
    permA = [0]*len(A)
    advantageA = [0]*len(A)
    Bsorted = B[:]
    Bsorted.sort()
    Bsorted.reverse()
    
    #we want perm A where each element is minimally larger than its counterpart in B
    #if an element in B is larger than any in A, we want maximally smaller counterpart in perm A
    for index, b in enumerate(Bsorted):
        if b >= tmpA[len(tmpA)-1]:
            permA[index] = tmpA.pop(0)
        else:
            permA[index] = tmpA.pop(binarySearchIndexMinimizeDiff(tmpA, b))
    
    #we need to "unsort" B and reorder our permA by this unsorting
    index = 0
    for b in B:
        i = Bsorted.index(b)
        Bsorted[i] = None
        advantageA[index] = permA[i]
        index = index + 1
        
    return advantageA

arr = [2,7,11,15]
target = 10
a = binarySearchIndexMinimizeDiff(arr, target=target)
print("Smallest e larger than {0} is {1}".format(target, arr[a]))
a = advantageCount([2,7,11,15], [1,10,4,11])
print(a)