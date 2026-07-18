class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set([i+1 for i in range(20)])

        for num in nums:
            if num in s:
                s.remove(num)
        
        return min(s)

        