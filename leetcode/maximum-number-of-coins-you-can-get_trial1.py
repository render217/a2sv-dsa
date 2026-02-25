class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        mine = 0
        piles.sort()
        l = 0
        r = len(piles) - 1
        while l < r:
            r-=1 # alice
            mine += piles[r] 
            l+=1 
            r-=1
        return mine