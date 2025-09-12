class Solution:

    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(c.lower() for c in s if s.isalnum())
        return s == s[::-1]

    def matrix(self, s: str) -> list[list[bool]]:
        n = len(s)
        m = [[False for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                m[i][j] = self.isPalindrome(s[i:j + 1])
        return m
    
    def minCut(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        f = [0 for i in range(n)]
        m = self.matrix(s)

        f[0] = 0
        for i in range(1, n):
            if m[0][i]:
                f[i] = 0
            else:
                data = [(f[i - 1] + 1)]
                for j in range(i):
                    if m[j + 1 : i]:
                        data.append(f[j] + 1)
                f[i] = min(data)
        
        return f[n - 1]

