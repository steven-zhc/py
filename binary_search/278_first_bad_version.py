# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n <= 1:
            return 1
        start, end = 1, n 
        while start + 1 < end:
            mid = (start + end) // 2

            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        
        if isBadVersion(start):
            return start
        else:
            return end
        