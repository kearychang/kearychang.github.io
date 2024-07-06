import math

class Solution:
    powerDict = {0:1}
    
    def myPow(self, x: float, n: int) -> float:
        if (n == 0):
            return 1
        elif (x == 0):
            return 0
        largestPowerOf2 = math.floor(math.log2(abs(n)))
        pow = 1
        if (n < 0):
            Solution.powerDict[1] = 1/abs(x)
        else:
            Solution.powerDict[1] = abs(x)
        while (pow <= largestPowerOf2):
            pow = pow + 1
            Solution.powerDict[pow] = Solution.powerDict[pow - 1] * Solution.powerDict[pow - 1]
        
        binStr = ''
        finalVal = 1
        if (n < 0):
            binStr = bin(n)[3:]
        else:
            binStr = bin(n)[2:]
            
        for i in range(len(binStr)):
            if (binStr[i] == '1'):
                finalVal = finalVal * Solution.powerDict[pow - i]
        
        if (x < 0 and n%2 == 1):
            return -finalVal
        return finalVal

x = Solution()
assert x.myPow(-13, 3) == 2**15