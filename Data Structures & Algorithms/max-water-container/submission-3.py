class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while l < r:
            area = 0
            if heights[l] < heights[r]:
                area = heights[l] * (r-l)
                l += 1
            else:
                area = heights[r] * (r-l)
                r -= 1
            # if heights[l+1] > heights[l]:
            #     l += 1
            # if heights[r-1] > heights[r]:
            #     r -= 1
            maxArea = max(maxArea, area)
        return maxArea