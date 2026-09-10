class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(goal, -1, -1):
            max_jump = nums[i]
            if i + max_jump >= goal:
                goal = i

        if goal == 0:
            return True
        else:
            return False