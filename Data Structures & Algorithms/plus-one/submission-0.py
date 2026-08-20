class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = ""

        for i in digits:
            total = total + str(i)

        total = int(total) + 1
        return list(str(total))