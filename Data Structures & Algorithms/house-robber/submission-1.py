class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)

        max_rob = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            curr = max(nums[i]+max_rob[i-2], max_rob[i-1])
            max_rob.append(curr)

        return max_rob[-1]