import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        heap = []
        for num in nums:
            seen[num] += 1
        for key in seen:
            heapq.heappush(heap, (seen[key], key))
        while len(heap) > k:
            heapq.heappop(heap)
        return [num for count, num in heap]
            