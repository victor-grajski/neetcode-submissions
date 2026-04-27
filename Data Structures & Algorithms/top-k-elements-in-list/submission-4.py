class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        pairs = []
        res = []

        for num in nums:
            seen[num] += 1
        
        for key in seen:
            pairs.append((seen[key], key))
        
        pairs_sorted = sorted(pairs, reverse=True)

        for i in range(k):
            res.append(pairs_sorted[i][1])
        return res
