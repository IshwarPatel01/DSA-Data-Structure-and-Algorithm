#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        #code here
        if n == 1:
            return 1
        x= n ** 3
        y = self.sumOfSeries(n -1)
        return x + y
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
        print("~")
# } Driver Code Ends