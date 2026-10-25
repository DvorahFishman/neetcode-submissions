class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for original_word in strs:
            count_word = [0]*26
            for char in original_word:
                count_word[ord(char) - 97] += 1
            key = tuple(count_word)
            if key not in word_dict:
                word_dict[key] = []
            word_dict[key].append(original_word)
        return list(word_dict.values())       
            
        



        