class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        count = 0

        for num in nums:
            if num == 1:
                i += 1
            if num == 0:
                if i > count:
                    count = i
                i = 0
                    
        
        if i > count:
            count = i

        return count
        