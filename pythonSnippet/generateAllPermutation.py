

def genStringPermutation(str, currStr):
    if len(str) == 0:
        print(currStr)
    else:
        for i in range(len(str)):
            substr = str[:i] + str[i+1:]
            genStringPermutation(substr, currStr + str[i])

genStringPermutation("ABCD", "")