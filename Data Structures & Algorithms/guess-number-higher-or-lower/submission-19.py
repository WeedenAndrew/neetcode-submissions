# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        guessed = False

        while guessed != True:
            g = (low + high) // 2
            res = guess(g)
            if res == 1:
                low = g + 1
            
            elif res == -1:
                high = g - 1
            
            if res == 0:
                guessed = True
                return g