class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # trimmed_string = s.rstrip()
        l_string = s.split()
        return len(l_string[-1])
        