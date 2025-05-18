#User function Template for python3

class Solution:
    def isPalindrome(self, n):
		# Code here
# 		left = 0
# 		right = str(len(n)) -1
		
# 		if left >= right:
# 		    return True
		
# 		if n[left] != n[right]:
# 		    return False
		
# 		return self.isPalindrome(n, left + 1, right - 1)

    
        s = str(n)

    # Reject negative numbers
        if s.startswith('-'):
            return False

    # Base case: empty or single char string is palindrome
        if len(s) <= 1:
            return True

    # If first and last char differ, not palindrome
        if s[0] != s[-1]:
            return False

    # Recurse on the substring without first and last char
        return self.isPalindrome(s[1:-1])

                


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())  # Number of test cases
    solution = Solution()

    for _ in range(T):
        n = int(input())  # Input number
        ans = solution.isPalindrome(n)
        print("true" if ans else "false")

        print("~")

# } Driver Code Ends