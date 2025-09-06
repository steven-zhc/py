class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            raise Exception("nums are empty")
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if nums[start] == nums[start + 1]:
                start += 1
            elif nums[start] < nums[mid]:
                start = mid
            else:
                end = mid
        
        return min(nums[0], nums[-1], nums[start], nums[end])