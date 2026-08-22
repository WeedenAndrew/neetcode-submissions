class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        
        post = 1
        for i in reversed(range(len(nums))):
            res[i] *= post
            post *= nums[i]
        return res