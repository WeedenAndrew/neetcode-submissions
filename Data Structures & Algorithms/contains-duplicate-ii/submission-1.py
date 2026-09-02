class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        distance = {}
        for i in range(len(nums)):
            if nums[i] in distance:
                if abs(distance[nums[i]] - i) <= k:
                    return True
            distance[nums[i]] = i 
        return False