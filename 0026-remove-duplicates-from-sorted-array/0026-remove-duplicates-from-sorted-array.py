class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        arr_set = sorted(set(nums))
        k = len(arr_set)

        for i in range(k):
            nums[i] = arr_set[i]
        
        return k
            


            



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not nums:
        #     return 0  # Edge case: empty array
    
        # i = 0  # Slow pointer for unique elements
    
        # for j in range(1, len(nums)):  # Fast pointer starts from index 1
        #     if nums[j] != nums[i]:  # Found a new unique element
        #         i += 1  # Move slow pointer
        #         nums[i] = nums[j]  # Overwrite duplicate
            
        # return i + 1  # Number of unique elements














