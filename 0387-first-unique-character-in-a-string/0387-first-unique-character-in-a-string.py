class Solution:
    def firstUniqChar(self, s: str) -> int:
        list_str = list(s)
        n = len(list_str)
        freq = {}
        for char in list_str:
            freq[char] = freq.get(char,0) + 1
        

        for i in range(n):
            if freq[list_str[i]] == 1:
                return i

        return -1
        