class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        for i in range(0,(len(nums) - 1)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
                    
# function twoSum(nums, target):
#     hash_map = {}  # To store numbers and their indices
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in hash_map:
#             return [hash_map[complement], i]  # Return indices of the pair
#         hash_map[num] = i  # Store the current number and its index
#     return []  # No solution found (though the problem guarantees one)
