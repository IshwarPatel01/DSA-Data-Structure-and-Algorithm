class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dist = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dist:
                return [dist[complement], i]
            
            dist[nums[i]] = i
        return []        