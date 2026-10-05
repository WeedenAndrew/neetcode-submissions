class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range((n//2) -1, -1, -1):
            root = i
            while root * 2 + 1 < n:
                child = root * 2 + 1
                if child + 1 < n and nums[child] < nums[child + 1]:
                    child += 1
                if nums[root] < nums[child]:
                    nums[root], nums[child] = nums[child], nums[root]
                    root = child
                else:
                    break

        
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]

            root = 0
            while root * 2 + 1 < i:
                child = root * 2 + 1
                if child + 1 < i and nums[child] < nums[child + 1]:
                    child += 1
                if nums[root] < nums[child]:
                    nums[root], nums[child] = nums[child], nums[root]
                    root = child
                else:
                    break
        
        return nums