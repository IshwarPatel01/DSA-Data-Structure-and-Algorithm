#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        # reversed_str = ""
        # for i in range(len(s)- 1, -1 , -1):
        #     reversed_str += s[i]
        
        # return reversed_str
            
        # reversed_str = []
         
        # for i in range(len(s) - 1, -1 , -1):
        #     reversed_str.append(s[i])
        # return "".join(reversed_str)
        
        # reversed_str = list(s)
        # left, right = 0, len(reversed_str) -1
        
        # while left < right:
        #     reversed_str[left],reversed_str[right] = reversed_str[right],reversed_str[left]
        #     left += 1
        #     right -= 1
            
        # return "".join(reversed_str)
        
        
        reversed_str = list(s)
        n = len(reversed_str)
        
        for i in range(n // 2):
            reversed_str[i], reversed_str[n- i- 1] = reversed_str[n- i- 1],reversed_str[i]
    
        return "".join(reversed_str)    
        
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        s = input()
        ob = Solution()
        print(ob.reverseString(s))
        t = t - 1

        print("~")

# } Driver Code Ends