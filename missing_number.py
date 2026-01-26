# https://leetcode.com/problems/missing-number/submissions/1895345201

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i