class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if not nums:
            return 0
    
        min_current = max_current = max_product = nums[0]
    
        for i in range(1, len(nums)):
        # If the current number is negative, swap min and max
            if nums[i] < 0:
                min_current, max_current = max_current, min_current
        
        # Update min_current without using the built-in min function
            if nums[i] < min_current * nums[i]:
                min_current = nums[i]
            else:
                min_current = min_current * nums[i]
        
        # Update max_current without using the built-in max function
            if nums[i] > max_current * nums[i]:
                max_current = nums[i]
            else:
                max_current = max_current * nums[i]
        
            # Update the overall maximum product
            if max_current > max_product:
                max_product = max_current
    
        return max_product