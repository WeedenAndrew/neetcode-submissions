class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swaps, i, j = 0, 0, len(nums) -1

        for i in range(len(nums)):
            if nums[i] == val:
                swaps += 1
        i=0

        while i < j:
            while nums[i] != val and i < j:
                i += 1

            while nums[j] == val and i < j:
                j -= 1
            
            if i>= j: break

            nums[i], nums[j] = nums[j], nums[i]
        
        return len(nums) - swaps