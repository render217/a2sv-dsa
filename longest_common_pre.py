# submission: https://leetcode.com/problems/longest-common-prefix/submissions/1895454177
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        shortest = min(strs, key=len)
        
        for i in range(len(shortest)):
            char = shortest[i]  
            for string in strs:
                if string[i] != char:
                    return shortest[:i]
    
        return shortest