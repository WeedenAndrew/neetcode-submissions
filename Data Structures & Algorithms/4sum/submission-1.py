class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def distinct(a, b, c, d):
            return a != b and a != c and a != d \
                    and b != c and b != d and c != d
            
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i

        s = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    desired = target - nums[i] - nums[j] - nums[k]
                    if desired in h and distinct(i, j, k, h[desired]):
                        t = tuple(sorted([nums[i], nums[j], nums[k], desired]))
                        s.add(t)
        
        return list(s)