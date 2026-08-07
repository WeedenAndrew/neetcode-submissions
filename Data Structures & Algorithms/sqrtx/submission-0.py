class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x

        while left <= right:
            mid = (left + right) // 2
            mid_Squared = mid * mid

            if mid_Squared == x:
                return mid
            elif mid_Squared < x:
                left = mid + 1
            else:
                right = mid - 1

        return right  