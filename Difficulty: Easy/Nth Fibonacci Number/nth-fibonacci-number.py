
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return self.nthFibonacci(n - 1) + self.nthFibonacci(n - 2)
        
