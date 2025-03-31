#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        if n < 2:
            return -1
        
        arr.sort()
        largest = arr[n - 1]
        second_largest = None
        for i in range(n-2, -1, -1):
            if arr[i] != largest:
                second_largest = arr[i]
                break
        
        if second_largest is None:
            return -1
        else:
            return second_largest
            
        # Code Here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends