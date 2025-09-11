class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        f = [0 for i in range(n)]
        f[0] = 1
        f[1] = 2
        for i in range(2, n):
            f[i] = f[i - 1] + f[i - 2]
        return f[n - 1]