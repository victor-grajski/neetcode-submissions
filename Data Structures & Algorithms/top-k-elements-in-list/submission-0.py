class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        most_frequent_elements = []
        for i, num in enumerate(nums):
            seen[num] += 1
        sorted_data = {k: v for k, v in sorted(seen.items(), key=lambda item: item[1], reverse=True)}
        return list(sorted_data)[0:k]

        