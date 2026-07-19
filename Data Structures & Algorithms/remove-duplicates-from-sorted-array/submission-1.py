class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        temp = nums.copy()
        for num in temp:
            print(num)
            if num not in seen:
                seen.append(num)
            elif num in seen:
                nums.remove(num)

        return len(nums)