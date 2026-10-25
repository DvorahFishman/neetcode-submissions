class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word)) 
            word_dict[sorted_word].append(word)                      
        return list(word_dict.values())
    
        

        

        