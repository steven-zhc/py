class Solution:    
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        n = len(nums)
        f = [False for i in range(n)]

        f[0] = True
        for i in range(1, n):
            for j in range(i):
                if f[j] and j+ nums[j] >= i:
                    f[i] = True
                    break
        
        return f[n - 1]