class Solution(object):
    def majorityElement(self, nums):

        item_present = {}
        
        for i in nums:
            if i not in item_present:
                item_present[i] = 1
            else:
                item_present[i] = item_present[i]+1
        
        value = [i for i in item_present if item_present[i] > (len(nums)/2)]
        return value[0]
        