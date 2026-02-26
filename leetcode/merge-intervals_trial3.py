class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda v: v[0])

        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if last[1] >= current[0]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
                
        return merged