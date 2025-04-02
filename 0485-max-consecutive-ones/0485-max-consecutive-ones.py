class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        long = 0
        count = 0
        
        for num in nums:
            if num == 1:
                count += 1
                long = max(long, count)
            else:
                count = 0
        return long
            

    #         class Solution:
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #     long = 0
    #     count = 0
    #     for val in nums:
    #         if val == 1:
    #             count += 1
    #             long = max(long, count) 
    #         else:
    #             count = 0
    #     return long


    # class Solution:
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #     count = 0
    #     top = 0
    #     for i in range(len(nums)):
    #         if nums[i] == 1:
    #             count += 1
    #         if nums[i] == 0:
    #             if count > top:
    #                 top = count
    #             count = 0

    #     if count > top:
    #         top = count

    #     return top
        