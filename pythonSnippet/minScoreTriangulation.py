from sys import maxsize

class Solution:
    minScoreDict = {}

    def minScoreTriangulation(self, A):
        if tuple(A) in self.minScoreDict:
            return self.minScoreDict[tuple(A)]
        elif len(A) == 3:
            return A[0] * A[1] * A[2]
        elif len(A) < 3:
            raise Exception("too few vertices")
        else:
            minVal = maxsize
            lenA = len(A)
            if lenA == 4:
                lenA = 2
            for i in range(0, lenA):
                totalSum = A[i]*A[(i+1)%len(A)]*A[(i+2)%len(A)]
                A_subset = A[:]
                A_subset.pop((i+1)%len(A_subset))
                totalSum += self.minScoreTriangulation(A_subset)
                minVal = min(minVal, totalSum)
            self.minScoreDict[tuple(A)] = minVal
            return minVal

    #WRONG
    '''
    def minScoreTriangulationBruteForce(self, A):
        if len(A) == 3:
            return A[0] * A[1] * A[2]
        elif len(A) < 3:
            raise Exception("too few vertices")
        else:
            minVal = maxsize
            for i in range(0, len(A)):
                print("{0}, {1}, {2}, {3}".format(A[i], A[(i+1)%len(A)], A[(i+2)%len(A)], A[i] * A[(i+1)%len(A)] *A[(i+2)%len(A)]))
                totalSum = A[i] * A[(i+1)%len(A)] * A[(i+2)%len(A)]
                for j in range(0, len(A)-3):
                    print("{0}, {1}, {2}, {3}".format(A[i], A[(i+j+2)%len(A)], A[(i+j+3)%len(A)], A[i] * A[(i+j+2)%len(A)] * A[(i+j+3)%len(A)]))
                    totalSum += (A[i] * A[(i+j+2)%len(A)] * A[(i+j+3)%len(A)])
                minVal = min(minVal, totalSum)
                print("total Sum - {0}".format(totalSum))
            return minVal
    '''
        
sol = Solution()
#print(sol.minScoreTriangulation([10,6,8,5,4]))
#print(sol.minScoreTriangulation([1,3,1,4,1,5]))
print(sol.minScoreTriangulation([38,76,69,32,24,35,82,30,86,77,92,3,35,20,84,67,23,58,94,10]))