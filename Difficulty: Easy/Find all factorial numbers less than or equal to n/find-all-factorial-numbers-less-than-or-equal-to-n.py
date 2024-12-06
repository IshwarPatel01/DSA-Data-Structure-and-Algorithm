class Solution:

    def factorialNumbers(self, n):
        fac = 1  # initialize the factorial to 1
        x = 2  # initialize x to 2
        ans = []  # create an empty list to store the factorial numbers
        while fac <= n:  # iterate until the factorial is less than or equal to N
            ans.append(fac)  # add the factorial to the list
            fac *= x  # calculate the next factorial by multiplying it with x
            x += 1  # increase the value of x by 1 for the next iteration
        return ans  # return the list of factorial numbers



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends