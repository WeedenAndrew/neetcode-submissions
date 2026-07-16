class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            dic[num] += 1
        
        print(max(dic))
        return max(dic, key=dic.get)
        