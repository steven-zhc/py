class Solution:
    def divide_conquer(self, triangle: list[list[int]], x: int, y: int, memo: dict[tuple[int, int], int]) -> int:
        if x == len(triangle):
            return 0
        
        if (x, y) in memo:
            return memo[(x, y)]
        
        left = self.divide_conquer(triangle, x + 1, y, memo)
        right = self.divide_conquer(triangle, x + 1, y + 1, memo)

        memo[(x, y)] = min(left, right) + triangle[x][y]
        return memo[(x, y)]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.divide_conquer(triangle, 0, 0, {})