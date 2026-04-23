class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        nums_sorted = sorted(nums)
        
        current_streak = 1
        longest_streak = 1

        for i in range(len(nums) - 1):
            if nums_sorted[i+1] - nums_sorted[i] == 1:
                current_streak += 1
                if current_streak > longest_streak:
                    longest_streak = current_streak
            elif nums_sorted[i+1] == nums_sorted[i]:
                continue
            else:
                current_streak = 1
        return longest_streak
        