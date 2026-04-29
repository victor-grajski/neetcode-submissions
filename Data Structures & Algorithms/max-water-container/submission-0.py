class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            area = 0

            r = i + 1
            while r < len(heights):
                if heights[r] > heights[i]:
                    area = heights[i] * (r-i)
                else:
                    area = heights[r] * (r-i)
                if area > max_area:
                    max_area = area
                r += 1
        return max_area
