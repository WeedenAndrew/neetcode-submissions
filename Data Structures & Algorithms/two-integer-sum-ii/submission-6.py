class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            if (numbers[left] + numbers[right]) < target:
                left += 1
            
            elif (numbers[left] + numbers[right]) > target:
                right -= 1
            
            else:
                print(left, right)
                return [numbers.index(numbers[left]) + 1, numbers.index(numbers[right]) + 1]
        
        return []


        # for i in range(len(numbers)):
        #     if (target - numbers[i]) in numbers:
        #         return [i+1, numbers.index((target - numbers[i]))+1]
        
        # return []