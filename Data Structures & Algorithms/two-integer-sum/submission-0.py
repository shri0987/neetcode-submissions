class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] not in difference_map.keys():
                difference_map[diff] = i
            else:
                result = [i, difference_map[nums[i]]] if i < difference_map[nums[i]] else [difference_map[nums[i]], i]
                return result
        