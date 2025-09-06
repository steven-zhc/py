class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True
            elif nums[start] == nums[mid]:
                start += 1
                continue
            elif nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
                
        if nums[start] == target or nums[end] == target:
            return True
        else:
            return False