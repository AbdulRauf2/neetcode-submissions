class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best = 0

        while left < right:
            width = right - left 
            area = width * min(heights[left], heights[right])
            best = max(best, area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] >= heights[right] :
                right -= 1
        return best

         