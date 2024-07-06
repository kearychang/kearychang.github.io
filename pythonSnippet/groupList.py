class Solution:
    def groupThePeople(self, groupSizes):
        groupDict = {}
        groupSet = set()
        for e in groupSizes:
            if e in groupDict:
                groupDict[e] += 1
            else:
                groupDict[e] = 1
            groupSet.add(e)
        
        duplicate = 0
        for n in groupSet:
            if groupDict[n] > n:
                duplicate += (groupDict[n]//n) - 1
        
        groupCount = len(groupSet) + duplicate
        return [[] for n in range(groupCount)]

x = Solution()
print(x.groupThePeople([3,3,3,1,3,3,3,1,3,3,3,2,2]))