class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if not word1:
            return n
        if not word2:
            return m
        
        f = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        f[0][0] = 0
        for i in range(1, m + 1):
            f[i][0] = i
        for i in range(1, n + 1):
            f[0][i] = i
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[:i] == word2[:j]:
                    f[i][j] = 0
                    continue
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1
        
        return f[m][n]