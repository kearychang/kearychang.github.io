import math

class Solution:
    def maxArea(self, height):
        lenHeight = len(height)
        leftIndex, rightIndex = 0, lenHeight-1
        maxVal = (lenHeight-1) * min(height[leftIndex], height[rightIndex])
        
        while True:
            reCheck = False
            for i in range(leftIndex + 1, rightIndex):
                if height[i] > height[leftIndex]:
                    leftIndex = i
                    reCheck = True
                    break
            if reCheck:
                for j in range(rightIndex, leftIndex, -1):
                    containerHeight = min(height[leftIndex], height[j])
                    containerWidth = j - leftIndex
                    area = containerHeight * containerWidth
                    if area > maxVal:
                        maxVal = area
                        break
            else:
                break

        leftIndex, rightIndex = 0, lenHeight-1
        while True:
            reCheck = False
            for j in range(rightIndex - 1, leftIndex, -1):
                if height[j] > height[rightIndex]:
                    rightIndex = j
                    reCheck = True
                    break
            if reCheck:
                for i in range(leftIndex, rightIndex):
                    x = height[i]
                    y = height[rightIndex]
                    containerHeight = min(height[i], height[rightIndex])
                    containerWidth = rightIndex - i
                    area = containerHeight * containerWidth
                    if area > maxVal:
                        maxVal = area
                        break
            else:
                break
        return maxVal

    def maxAreaBruteForce(self, height):
        lenHeight = len(height)
        maxVal = (lenHeight-1) * min(height[0], height[lenHeight - 1])
        for i in range(0, lenHeight - 2):
            for j in range(lenHeight - 1, i, -1):
                containerHeight = min(height[i], height[j])
                containerWidth = j - i
                area = containerHeight * containerWidth
                maxVal = max(maxVal, area)
        return maxVal

sol = Solution()
#print(sol.maxAreaBruteForce([10,9,8,7,6,5,4,3,2,1])