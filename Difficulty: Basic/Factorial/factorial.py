#User function Template for python3


class Solution:
    def factorial (self, n):
        # code here
        
        if n == 0:
            return 1
        # result *= n
        return n * self.factorial(n - 1)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.factorial(n))

        print("~")

# } Driver Code Ends