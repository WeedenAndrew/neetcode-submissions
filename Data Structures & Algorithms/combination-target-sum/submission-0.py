class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, sol = [], []

        def backtrack(i):
            if sum(sol) == target:
                ans.append(sol[:])
                return
            
            if i == len(nums) or sum(sol) > target:
                return
            
            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i)
            sol.pop()

        backtrack(0)
        return ans