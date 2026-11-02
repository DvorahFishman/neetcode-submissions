class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        max_freq = max(freq_dict.values(), default=0)
        if max_freq > 1:
            return True
        return False