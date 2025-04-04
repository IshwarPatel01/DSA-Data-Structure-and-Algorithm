class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hash_map = {}

        for i in nums:
            hash_map[i] = True

        for i in range(n):
            if i not in hash_map:
                return i
            
        return n



        