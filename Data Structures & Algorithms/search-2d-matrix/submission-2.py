class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        left, right = 0, (r * c) - 1
        
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // c, mid % c
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False