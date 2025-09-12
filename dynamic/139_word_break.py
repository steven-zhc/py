def fun2():

class Solution:
    def fun1(self):
        return True
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        
        n = len(s)
        
        memo = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):   # j must start >= i
                if s[i:j+1] in wordDict:
                    memo[i][j] = True
        
        f = [False] * n
        f[0] = s[0:1] in wordDict

        for i in range(1, n):
            if memo[0][i]:
                f[i] = True
            else:
                for j in range(i):
                    if f[j] and memo[j + 1][i]:
                        f[i] = True
                        break
        return f[n - 1]

