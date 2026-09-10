class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0

        for i in range(len(nums)):
            if i > curr:
                return False
            curr = max(curr, i + nums[i])
        return curr >= len(nums) - 1