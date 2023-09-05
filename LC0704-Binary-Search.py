class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 # <-- use strict boundary
        while left <= right:
            mid = left + (right - left) // 2 # avoid leak
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 # narrow down the boundary
            else:
                right = mid - 1
        return -1
