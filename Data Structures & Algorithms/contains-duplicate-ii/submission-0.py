class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_i = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in num_to_i:
                if abs(num_to_i[nums[i]] -i) <= k:
                    return True
            num_to_i[nums[i]] = i

        return False