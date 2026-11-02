class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            num_set.add(num)
        if len(num_set) != len(nums):
            return True
        return False