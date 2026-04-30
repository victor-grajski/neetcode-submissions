class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            left[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1 , -1):
            right[i] = suffix
            suffix *= nums[i]
        
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        return res
        