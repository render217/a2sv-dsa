# submission: https://leetcode.com/problems/contains-duplicate/submissions/1895446080

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)