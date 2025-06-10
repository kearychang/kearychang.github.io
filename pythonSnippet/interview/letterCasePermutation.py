def letterCasePermutation(S):
    countLetter = 0
    letterPos = []
    for i in range(len(S)):
        if not S[i].isdigit():
            countLetter += 1
            letterPos.append(i)
            
    permutationList = []
    byteArrayS = bytearray(S, "utf-8")
    for i in range(0, 2**countLetter):
        bitstr = bin(i)[2:].zfill(countLetter)
        byteArrayS_tmp = byteArrayS[:]
        for j in range(countLetter):
            if bitstr[j] == "1":
                c = chr(byteArrayS_tmp[letterPos[j]])
                byteArrayS_tmp[letterPos[j]] = ord(c.upper())
        permutationList.append(byteArrayS_tmp.decode("utf-8"))
    return permutationList

#print(letterCasePermutation("a1b2"))
print(letterCasePermutation("cf13f156q3t65yq3"))