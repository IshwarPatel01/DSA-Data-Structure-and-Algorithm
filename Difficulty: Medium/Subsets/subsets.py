#User function Template for python3

class Solution:
    def subsets(self, arr):
 
        arr.sort()  # Step 1: Sort the array
        result = []

        def backtrack(start, path):
            result.append(path[:])  # Add the current subset
            for i in range(start, len(arr)):
                path.append(arr[i])             # Choose
                backtrack(i + 1, path)          # Explore
                path.pop()                      # Un-choose (backtrack)

        backtrack(0, [])
        return result
