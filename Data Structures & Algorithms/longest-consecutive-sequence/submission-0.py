class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_streak = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                start = num
                current_streak = 1
                while start + current_streak in nums_set:
                    current_streak += 1
                max_streak = max(max_streak, current_streak)
        return max_streak