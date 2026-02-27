class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
         points.sort(key=lambda x : (x[0],x[1]))
         max_width = float('-inf')
         for i in range(len(points)-1):
            if abs(points[i+1][0] - points[i][0]) > max_width:
                max_width = points[i+1][0] - points[i][0]
         return max_width