class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        d = {}
        n = len(nums)
        for i, num in enumerate(nums):
            d[num] = i
        

        for i in range(n):
            for j in range(i+1, n):
                k = -(nums[i] + nums[j])
                if k in d and d[k] != i and d[k] != j:
                    triple = sorted([nums[i], nums[j], k])
                    triple = tuple(triple)
                    ans.add(triple)
        
        return list(ans)