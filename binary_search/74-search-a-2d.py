class Solution: 
    def pos(self, index: int, n: int) -> tuple[int, int]:
        return (
            index // n , index % n)
    
    def pos_curry(self, n: int):
        return lambda index: (index // n, index % n)
    
    def val(self, index: int, matrix: list[list[int]]) -> int:
        x, y = self.pos(index, len(matrix[0]))
        return matrix[x][y]
    
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False
        
        start, end = 0, len(matrix) * len(matrix[0]) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            v = self.val(mid, matrix)
            
            if v == target:
                return True
            elif v < target:
                start = mid
            else:
                end = mid
        
        if self.val(start, matrix) == target:
            return True
        elif self.val(end, matrix) == target:
            return True
        else:
            return False
