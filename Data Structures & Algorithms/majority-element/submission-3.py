class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidiate = None
        count = 0

        for num in nums:
            if count == 0:
                candidiate = num
            
            count += 1 if candidiate == num else -1

        return candidiate 