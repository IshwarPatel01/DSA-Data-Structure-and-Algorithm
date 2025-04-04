class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dist = {}
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in dist:
        #         return [dist[complement], i]
            
        #     dist[nums[i]] = i
        # return []    
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        n = len(nums)
        left = 0
        right = n - 1
        nums_with_index.sort()

        while left < right:
            summ = nums_with_index[left][0] + nums_with_index[right][0]
            if target == summ:
                return [nums_with_index[left][1] , nums_with_index[right][1]]
            elif target < summ:
                right -= 1
            else:
                left += 1
        return []   

