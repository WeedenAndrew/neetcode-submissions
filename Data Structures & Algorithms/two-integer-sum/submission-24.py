class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}

        for i, n in enumerate(nums):
            dif = target - n
            if dif in Map:
                return[Map[dif], i]
            Map[n] = i
        
        return []