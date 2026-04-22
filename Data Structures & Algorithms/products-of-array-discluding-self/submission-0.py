class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [None] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if products[i] is None:
                        products[i] = nums[j]
                    else:
                        products[i] *= nums[j]
        return products