
# https://leetcode.com/problems/smallest-even-multiple/submissions/1894686913

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n * 2