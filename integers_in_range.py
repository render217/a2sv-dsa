# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/submissions/1894696590

class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        ans = []
        for i in range(left, right + 1):
            temp = False
            for r in ranges:
                if r[0] <= i <= r[1]:
                    temp = True
                    break
            ans.append(temp)
        return all(ans)