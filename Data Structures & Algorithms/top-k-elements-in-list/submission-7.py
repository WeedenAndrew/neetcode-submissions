class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = {}

        for i in nums:
            if i not in top:
                top[i] = 1
            else:
                top[i] +=1

        return heapq.nlargest(k, top, key=top.get)
        