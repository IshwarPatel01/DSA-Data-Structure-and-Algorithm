
class Solution:
    def seriesSum(self, n : int) -> int:
        if n == 1:
            return 1 
        return n + self.seriesSum(n - 1)
        
