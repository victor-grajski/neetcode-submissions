class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen[num] += 1
        return False
