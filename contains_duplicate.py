# problem: https://www.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1

class Solution:
    def checkEqual(self, a, b) -> bool:
        if len(a) != len(b):
            return False
        a.sort()
        b.sort()
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True