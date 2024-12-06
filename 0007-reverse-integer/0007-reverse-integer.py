class Solution(object):
    def reverse(self, x):
        # Handling negative numbers
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        revNum = 0
        while x > 0:
            ld = x % 10  # Get the last digit
            x = x // 10  # Remove the last digit from x
            revNum = (revNum * 10) + ld  # Add the digit to the reversed number
        
        # Reapply the sign
        revNum *= sign
        
        # Handle overflow (32-bit signed integer range)
        if revNum < -2**31 or revNum > 2**31 - 1:
            return 0
        
        return revNum

        