class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = 0
        indices = []

        for i in range(0, len(nums)):
            total = nums[i]
            
            for j in range(i + 1, len(nums)):
                total += nums[j]
                
                if total == target:
                    indices.append(i)
                    indices.append(j)
                    return indices
                else:
                    total -= nums[j]


        return indices