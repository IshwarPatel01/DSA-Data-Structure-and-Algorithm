class Solution(object):
    def twoSum(self, nums, target):
        # seen = {}
        # for i, num in enumerate(nums):
        #     needed = target - num
        #     if needed in seen:
        #         return [seen[needed], i]
        #     seen[num] = i
        # return none
        for num in range(len(nums)):
            for i in range(num + 1, len(nums)):
                if nums[num] + nums[i] == target:
                    return [num , i]

       
        