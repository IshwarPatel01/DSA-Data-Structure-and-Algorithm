class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # hash_map = {}

        # for i in nums:
        #     hash_map[i] = True

        # for i in range(n):
        #     if i not in hash_map:
        #         return i
            
        # return n

        # n = len(nums)

        # for i in range(n + 1):
        #     flag = 0
        #     for j in range(n):
        #         if i == nums[j]:
        #             flag = 1
        #             break
        #     if flag == 0:
        #         return i
        
        # n = len(nums)
        # hash_map = [0] * (n + 1)
        # for i in nums:
        #     hash_map[i] = 1
        # for i in range(n):
        #     if hash_map[i] != 1:
        #         return i
        # return n
        
        n = len(nums)

        expected_sum = n * (n + 1) // 2 

        actual_sum = sum(nums)
        return expected_sum - actual_sum
        


        