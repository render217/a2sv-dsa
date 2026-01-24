# problem https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1
class Solution:
    def isSubset(self, a:list[int], b:list[int])->bool:
        if len(b) > len(a):
            return False
        freq = {}
        for num in a: 
            freq[num] = freq.get(num,0) + 1
        
        for num in b: 
            if freq.get(num,0) == 0:
                return False 
            freq[num] -=1
        return True