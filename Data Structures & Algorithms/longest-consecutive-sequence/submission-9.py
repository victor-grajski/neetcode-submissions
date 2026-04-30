class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        seen = {}

        for i, num in enumerate(nums):
            seen[num] = i

        for i, num in enumerate(nums):
            if num - 1 not in seen:
                current_streak = 1
                while num + current_streak in seen:
                    current_streak += 1
                longest_streak = max(current_streak, longest_streak)

        return longest_streak
        