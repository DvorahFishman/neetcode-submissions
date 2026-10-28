class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        maxlength = 0 
        freq_set = set()
        for char in s:
            while char in freq_set:
                freq_set.remove(s[left])
                left += 1
            freq_set.add(char)
            maxlength = max(maxlength, len(freq_set))
        return maxlength