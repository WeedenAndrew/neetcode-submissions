class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0

        while t != target:
            if target in matrix[t]:
                t = target
                return True
            elif t == len(matrix) - 1:
                break
            t += 1
        return False