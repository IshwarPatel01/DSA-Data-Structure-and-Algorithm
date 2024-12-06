#User function Template for python3

class Solution:
    def sumOfDivisors(self, n):
        # Create an array to store the sum of divisors for each number from 1 to n
        divisors_sum = [0] * (n + 1)
        
        # Loop over each number to calculate divisors sum
        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                divisors_sum[j] += i
        
        # Sum up all divisors sums from 1 to n
        total_sum = sum(divisors_sum[1:])
        
        return total_sum



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
        print("~")

# } Driver Code Ends