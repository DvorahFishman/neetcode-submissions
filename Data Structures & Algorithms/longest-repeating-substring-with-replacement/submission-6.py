class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        counts = [0] * 26
        max_freq = 0
        for right, char in enumerate(s):
            char_idx = ord(char) - ord('A')
            counts[char_idx] += 1
            max_freq = max(max_freq, counts[char_idx])
            if (right - left + 1) - max_freq > k:
                left_char_idx = ord(s[left]) - ord('A')
                counts[left_char_idx] -= 1
                left += 1 
            max_length = max(max_length, right - left + 1)  
        return max_length