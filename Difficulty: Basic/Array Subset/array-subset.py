#User function Template for python3

from collections import defaultdict


class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        #creating two dictionaries to store the frequency of each element in a and b.
        dic1 = defaultdict(lambda: 0)

        #iterating over a and updating the frequency in dic1.
        for i in a:
            dic1[i] += 1

        #iterating over b and checking if the frequency of each element in b is greater than 0 in dic1.
        for i in b:
            if dic1[i] > 0:
                dic1[i] -= 1
            else:
                return False

        return True



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        ob = Solution()
        if ob.isSubset(a1, a2):
            print("Yes")
        else:
            print("No")

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends