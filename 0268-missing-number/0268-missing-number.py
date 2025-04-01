class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hash_map = [0] * (n + 1)

        for i in range(len(nums)):
            hash_map[nums[i]] += 1
        
        for i in range(len(hash_map)):
            if hash_map[i] == 0:
                return i
            
        return len(hash_map)



        