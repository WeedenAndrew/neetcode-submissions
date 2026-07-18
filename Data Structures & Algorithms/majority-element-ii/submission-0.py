class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        top = []
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        for i in dic.keys():
            if dic[i] > (len(nums)//3):
                top.append(i)

        return top