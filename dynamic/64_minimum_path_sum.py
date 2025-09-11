class Solution:
    def divide_conquer(self, grid: List[List[int]], m: int, n: int, x: int, y: int, memo: dict[(int, int), int]) -> int:
        if not grid:
            return 0
        if (x, y) in memo:
            return memo[(x, y)]
        result = []
        if x + 1 < m:
            right = self.divide_conquer(grid, m, n, x + 1, y, memo)
            result.append(right)
        if y + 1 < n:
            bottom = self.divide_conquer(grid, m, n, x, y + 1, memo)
            result.append(bottom)

        if result:
            memo[(x, y)] = min(result) + grid[x][y]
        else:
            memo[(x, y)] = grid[x][y]
        return memo[(x, y)]


    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        return self.divide_conquer(grid, m, n, 0, 0, {})