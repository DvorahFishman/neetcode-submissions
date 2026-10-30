class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        up = 0
        down = m - 1
        while up <= down:
            mid_row = (up + down)//2
            if matrix[mid_row][0] == target:
                return True
            if matrix[mid_row][0] > target:
                down = mid_row - 1
            else:
                up = mid_row + 1

        if down < 0: 
            return False
                              
        left = 0 
        right = n -1
        while left <= right:
            mid = (left + right)//2
            if matrix[down][mid] == target:
                return True
            if matrix[down][mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return False

         