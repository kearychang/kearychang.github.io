def canFormArray(arr, pieces):
    pieceSet = set()
    for subArr in pieces:
        for e in subArr:
            pieceSet.add(e)
    arrSet = set(arr)
    return len(pieceSet - arrSet) == 0

print(canFormArray([49,18,16], [[16,18,49]]))