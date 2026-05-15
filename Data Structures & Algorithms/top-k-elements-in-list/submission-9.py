import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for i, num in enumerate(nums):
            seen[num] += 1
        heap = []
        for key in seen:
            heapq.heappush(heap, (seen[key], key))
        while len(heap) > k:
            heapq.heappop(heap)
        res = []
        for item in heap:
            res.append(item[1])
        return res
