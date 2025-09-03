class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        start, end = 1, x - 1
        while start + 1 < end:
            mid = (start + end) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                start = mid
            else:
                end = mid

        if end * end <= x:
            return end
        else:
            return start