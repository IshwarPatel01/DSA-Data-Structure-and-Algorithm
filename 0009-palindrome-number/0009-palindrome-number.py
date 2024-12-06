class Solution(object):
    def isPalindrome(self, x):
        dup = x
        revNum = 0
        while x > 0:
            ld = x % 10
            x = x // 10
            revNum = (revNum * 10) + ld
        if revNum == dup:
            return True
        else: 
            return False
        