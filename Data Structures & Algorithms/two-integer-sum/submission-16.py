class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []

        complement = target
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                res.append(seen[complement])
                res.append(i)
            else:
                seen[num] = i
        return res
        