class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        ROWS, COLS = len(matrix), len(matrix[0])
        low, high = 0, (ROWS * COLS) - 1
        
        while low <= high:
            mid = (low + high) // 2
            # Map the 1D index back to 2D row and column
            mid_element = matrix[mid // COLS][mid % COLS]
            
            if mid_element == target:
                return True
            elif mid_element < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False