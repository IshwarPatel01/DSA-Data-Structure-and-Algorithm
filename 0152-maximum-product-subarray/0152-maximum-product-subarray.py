# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
    
#         max_product = nums[0]  # Initialize the result with the first element
    
#     # Outer loop: starting index of the subarray
#         for i in range(len(nums)):
#             current_product = 1  # Reset current_product for each new starting index
        
#         # Inner loop: ending index of the subarray
#             for j in range(i, len(nums)):
#                 current_product *= nums[j]  # Multiply the current element
            
#             # Update max_product if the current_product is greater
#                 if current_product > max_product:
#                     max_product = current_product
    
#         return max_product



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_current = nums[0]
        min_current = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):
            current_value = nums[i]

            if current_value < 0:  # check negative value
                temp = max_current
                max_current = min_current
                min_current = temp
            
            if current_value > max_current * current_value:
                max_current = current_value 
            else: 
                max_current *= current_value
            
            if current_value < min_current * current_value:
                min_current = current_value
            else:
                min_current *= current_value

            if max_product < max_current:
                max_product = max_current

        return max_product

