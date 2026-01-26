# hhttps://leetcode.com/problems/find-players-with-zero-or-one-losses/submissions/1897918386
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = {}
        loses = {}
        for m in matches:
            wins[m[0]] = wins.get(m[0],0) + 1
            loses[m[1]] = loses.get(m[1],0) + 1
        ans1 = []
        for k in wins.keys():
            if k not in loses.keys():
                ans1.append(k)
        ans2 = []
        for k,v in loses.items():
            if v == 1:
                ans2.append(k)
        
        ans1.sort()
        ans2.sort()
        return [ans1,ans2]