import math

def numTilePossibilities(tiles):
    #init dict
    letterCountDict = {}
    for l in tiles:
        if l in letterCountDict:
            letterCountDict[l] += 1
        else:
            letterCountDict[l] = 1
    
    #get permutation denom to divide by for duplicate letters
    duplicateDenominator = 1
    for n in list(letterCountDict.values()):
        duplicateDenominator *= math.factorial(n)
    uniqueLetterCount = len(letterCountDict.keys())
    
    #get count for each sequence of n length
    totalCount = 0
    tilesCount = len(tiles)
    tilesPermutation = math.factorial(tilesCount)
    for i in range(1, tilesCount + 1):
        if i==1:
            count = uniqueLetterCount
        else:
            count = tilesPermutation//math.factorial(tilesCount-i)//duplicateDenominator
        totalCount += count
    return totalCount

print(numTilePossibilities("AAABBC"))