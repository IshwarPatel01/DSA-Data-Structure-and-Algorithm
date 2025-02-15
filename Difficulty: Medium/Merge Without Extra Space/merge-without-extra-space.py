class Solution:

    def mergeArrays(self, a, b):
        # Initialize pointer 'i' to the last index of array 'a'
        i = len(a) - 1
        # Initialize pointer 'j' to the first index of array 'b'
        j = 0

        # Loop until either 'i' goes out of bounds of 'a' or 'j' exceeds bounds of 'b'
        # Also, continue looping as long as the current element in 'a' is greater than
        # the current element in 'b'
        while i >= 0 and j < len(b) and a[i] > b[j]:
            # Swap the elements a[i] and b[j]
            a[i], b[j] = b[j], a[i]
            # Decrement 'i' to move to the previous element in 'a'
            i -= 1
            # Increment 'j' to move to the next element in 'b'
            j += 1

        # After swapping, sort array 'a' to ensure its elements are in non-decreasing order
        a.sort()
        # Similarly, sort array 'b' to ensure its elements are in non-decreasing order
        b.sort()



#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

        print("~")

# } Driver Code Ends