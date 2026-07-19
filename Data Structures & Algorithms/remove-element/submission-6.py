class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = nums.copy()

        for i in range(len(temp)):
            if temp[i] == val:
                nums.remove(temp[i])

        return len(nums)