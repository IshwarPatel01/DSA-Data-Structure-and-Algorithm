class Solution:
    def firstUniqChar(self, s: str) -> int:
        # list_str = list(s)
        # n = len(list_str)
        freq = {}
        for char in s:
            freq[char] = freq.get(char,0) + 1
        

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1
        