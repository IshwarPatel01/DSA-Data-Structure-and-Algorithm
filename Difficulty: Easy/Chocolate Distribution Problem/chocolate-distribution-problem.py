#User function Template for python3

class Solution:

    def findMinDiff(self, arr,M):

        # code here
        if M == 0 or len(arr) == 0:
            return 0
        
        arr.sort()
        
        n = len(arr)
        
        if M > n:
            return -1
        
        min_diff = float('inf')
        
        for i in range(n - M + 1):
            diff = arr[i + M - 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        
        return min_diff

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        A = [int(x) for x in input().split()]
        M = int(input())

        solObj = Solution()

        print(solObj.findMinDiff(A, M))
        print("~")

# } Driver Code Ends