class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # freq1 = {} 
        # freq2 = {}
        # for char in ransomNote:
        #     freq1[char] = freq1.get(char,0) + 1
        
        # for char in magazine:
        #     freq2[char] = freq2.get(char,0) + 1

        # for char in freq1:
        #     if freq1[char] > freq2.get(char, 0):
        #         return False
        # return True

        
        freq = {}

        for char in magazine:
            freq[char] = freq.get(char,0) + 1

        for char in ransomNote:
            if freq.get(char,0) == 0:
                return False
            freq[char] -= 1
        
        return True


