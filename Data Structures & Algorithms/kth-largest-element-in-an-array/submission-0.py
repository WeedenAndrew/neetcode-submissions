import heapq as h

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            h.heappush(heap, num)
            if len(heap) > k:
                h.heappop(heap)

        return heap[0]