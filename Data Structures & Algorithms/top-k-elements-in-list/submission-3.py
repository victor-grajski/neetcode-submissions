import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        heap = []
        for num in nums:
            seen[num] += 1
        for key in seen:
            if len(heap) < k:
                heapq.heappush(heap, (seen[key], key))
            else:
                if seen[key] > heap[0][0]:
                    heapq.heappushpop(heap, (seen[key], key))

        return [num for count, num in heap]