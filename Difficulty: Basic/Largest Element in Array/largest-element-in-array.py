
from typing import List


class Solution:
    def largest(self, arr):
        # code here
        largest_element = arr[0]
        if not arr:
            return 0
        for i in range(1, len(arr)):
            if largest_element < arr[i]:
                largest_element = arr[i]
        return largest_element
        
        # for i in range(len(arr)- 1):
        #     for j in range(i + 1,len(arr)):
                
    
                



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().split()))

        obj = Solution()
        res = obj.largest(arr)

        print(res)
        print("~")

# } Driver Code Ends