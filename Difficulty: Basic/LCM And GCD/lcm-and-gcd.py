#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List
import math


# } Driver Code Ends

#User function Template for python3
from math import gcd

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        
        gcd_value = gcd(a, b)
    
    # Calculate the LCM using the formula: LCM(a, b) = |a * b| / GCD(a, b)
        lcm_value = abs(a * b) // gcd_value

        return [lcm_value, gcd_value]

#{ 
 # Driver Code Starts.


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        a = int(input())
        b = int(input())
        obj = Solution()
        res = obj.lcmAndGcd(a, b)
        print(f"{res[0]} {res[1]}")
        print("~")

# } Driver Code Ends