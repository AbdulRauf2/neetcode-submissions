class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)

        merged = []
        start = 0
        end = 0
        
        for i in sorted_intervals:
            start = i[0]
            end = i[1]
            if merged and start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start,end])
        return merged