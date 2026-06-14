class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapping = dict()
        for val in nums:
            if val not in mapping.keys():
                mapping[val] = 1
            else:
                return True
        return False
        