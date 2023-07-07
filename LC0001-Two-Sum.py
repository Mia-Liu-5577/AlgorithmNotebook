class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index_map = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in value_to_index_map:
                return [value_to_index_map[remaining], i]
            # Put this at the end of each iteration
            # e.g. [3,2,4], target = 6
            value_to_index_map[nums[i]] = i
        return [-1, -1]
