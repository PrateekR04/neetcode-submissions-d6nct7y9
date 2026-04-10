class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        curArea = 0
        maxArea = float('-inf')

        while start < end:
            
            curArea = min(heights[start],heights[end]) * (end - start )

            if curArea > maxArea:
                maxArea = curArea
            
            if heights[start] > heights[end]:
                end = end - 1
            else:
                start += 1
        return maxArea