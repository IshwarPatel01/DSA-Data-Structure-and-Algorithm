# Back-end complete function Template for Python 3


class Solution:
    # Function to find the missing number in the array
    def missingNumber(self, arr):
        n = len(arr) + 1  # n is the expected size (size of arr + 1)
        total = (
            n * (n + 1)
        ) // 2  # calculate the sum of numbers from 1 to n using arithmetic progression formula
        sum_of_A = sum(arr)  # calculate the sum of all numbers in the array
        return total - sum_of_A  # return the missing number



#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends