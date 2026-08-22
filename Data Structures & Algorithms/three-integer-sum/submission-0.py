class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        d = {}
        n = len(nums)
        for i, num in enumerate(nums):
            d[num] = i
        

        for i in range(n):
            for j in range(i+1, n):
                z = -(nums[i] + nums[j])
                if z in d and d[z] != i and d[z] != j:
                    triple = sorted([nums[i], nums[j], z])
                    triple = tuple(triple)
                    ans.add(triple)
        
        return list(ans)