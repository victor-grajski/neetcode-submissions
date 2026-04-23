class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        if len(nums) == 0: return 0
        longest_streak = 1
        current_streak = 1
        for i in range(len(nums_sorted) - 1):
            if nums_sorted[i+1] - nums_sorted[i] == 1:
                current_streak += 1
                if current_streak > longest_streak:
                    longest_streak = current_streak
            if nums_sorted[i+1] == nums_sorted[i]:
                continue
            if nums_sorted[i+1] - nums_sorted[i] > 1:
                current_streak = 1

        return longest_streak
        