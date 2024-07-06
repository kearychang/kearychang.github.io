from itertools import combinations

class Solution:
    def bestTeamScore(self, scores, ages) -> int:
        ageSortList_sorted = sorted(zip(ages, scores))
        playerNotCompatibleDict = [[] for i in range(len(ageSortList_sorted))]
        playerCompatibleDict = [[] for i in range(len(ageSortList_sorted))]
        for i in range(len(ageSortList_sorted)):
            for j in range(len(ageSortList_sorted)):
                if not i == j:
                    t_i = ageSortList_sorted[i]
                    t_j = ageSortList_sorted[j]
                    if (t_i[0] <= t_j[0] and t_i[1] <= t_j[1]) or (t_i[0] >= t_j[0] and t_i[1] >= t_j[1]):
                        playerCompatibleDict[i].append(j)
                    else:  
                        playerNotCompatibleDict[i].append(j)
        #[set(C,D),set(B),set(E),set(),set()]
        
        stack = [0]
        alreadyAdded = [False]*len(ageSortList_sorted)
        maxScore = 0
        while len(stack) > 0:
            playerNumber = stack.pop(0)
            score = ageSortList_sorted[playerNumber][1]
            alreadyAdded[playerNumber] = True
            for p in playerNotCompatibleDict[playerNumber]:
                if not alreadyAdded[p]:
                    stack.append(p)
            for player in playerCompatibleDict[playerNumber]:
                score += ageSortList_sorted[player][1]
            maxScore = max(maxScore, score)
        return maxScore

sol = Solution()
print(sol.bestTeamScore([9,2,8,8,2], [4,1,3,3,5]))