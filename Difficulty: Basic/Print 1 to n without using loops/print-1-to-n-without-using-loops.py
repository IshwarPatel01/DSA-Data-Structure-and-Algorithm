#User function Template for python3

class Solution:
    def printTillN(self, n):
        if n == 0:
            return 
        self.printTillN(n - 1)
        print(n, end = " ")
        
    	#code here 