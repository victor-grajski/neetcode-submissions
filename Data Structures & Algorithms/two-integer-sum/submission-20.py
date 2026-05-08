class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []

        for i, num in enumerate(nums):
            seen[num] = i
        for i, num in enumerate(nums):
            gap = target - num
            if gap in seen and seen[gap] != i:
                return [i, seen[gap]]
        return []