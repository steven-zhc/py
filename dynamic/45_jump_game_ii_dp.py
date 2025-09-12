class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        f = [float('inf') for i in range(n)]
        f[0] = 0

        for i in range(1, n):
            p = []
            for j in range(0, i):
                if j + nums[j] >= i:
                    p.append(f[j] + 1)
            if not p:
                return 0
            else:
                f[i] = min(p)
        
        return f[n - 1]
