from collections import Counter

class Solution:
    def threeSumMulti(self, arr, target):
        c = Counter()
        for e in arr:
            c[e] += 1
        
        numList = list(c.keys())
        numList.sort()
        numListX = filter(lambda e:e <= target//3, numList)
        s = set(numList)

        count = 0
        for x in numListX:
            numListY = filter(lambda e:e >= x and e <= (target-x)//2, numList)
            for y in numListY:
                doubleXY = False
                doubleYZ = False
                triple = False
                if x == y:
                    if c[y] <= 1:
                        continue
                    else:
                        doubleXY = True
                z = target - x - y
                if z in s:
                    if z == y and z != x:
                        if c[z] <= 1:
                            continue
                        else:
                            doubleYZ = True
                    elif z == x:
                        if c[z] <= 2:
                            continue
                        else:
                            triple = True
                    if triple:
                        count = count + (c[x] * (c[x]-1) * (c[x]-2)//6)
                    elif doubleXY:
                        count = count + ((c[x] * (c[x]-1)//2) * c[z])
                    elif doubleYZ:
                        count = count + ((c[y] * (c[z]-1)//2) * c[x])
                    else:
                        count = count + (c[x] * c[y] * c[z])
        return count % (10**9 + 7)

sol = Solution()
print(sol.threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))
#print(sol.threeSumMulti([1,1,2,2,2,2], 5))