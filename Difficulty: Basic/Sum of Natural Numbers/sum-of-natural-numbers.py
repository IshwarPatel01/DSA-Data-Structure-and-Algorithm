
class Solution:
    def seriesSum(self, n : int) -> int:
        if n == 0:
            return 0
        return n + self.seriesSum(n - 1)
        
