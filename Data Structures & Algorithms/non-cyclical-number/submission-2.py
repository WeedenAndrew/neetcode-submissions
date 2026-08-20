class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = n

        while curr not in seen:
            seen.add(curr)
            summ = 0
            for digit in str(curr):
                summ += int(digit) **2

            if summ == 1: return True
            curr = summ

        return False