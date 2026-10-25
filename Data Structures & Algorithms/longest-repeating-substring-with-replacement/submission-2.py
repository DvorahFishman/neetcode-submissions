class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_length = 0
        count_dict = {}
        max_freq = 0
        for right, char in enumerate(s):
            count_dict[char] = count_dict.get(char, 0) + 1
            max_freq = max(max_freq, count_dict[char])
            if (right - left + 1) - max_freq > k:
                count_dict[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length