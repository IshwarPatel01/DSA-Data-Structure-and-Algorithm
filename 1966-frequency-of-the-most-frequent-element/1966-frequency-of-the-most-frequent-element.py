from collections import defaultdict

class Solution:
    def maxFrequency(self, nums, k):
        # Sort the array
        nums.sort()
        
        left = 0
        current_sum = 0
        max_freq = 0
        
        # Sliding window approach
        for right in range(len(nums)):
            # Calculate how many increments needed to bring nums[right] to the left elements
            current_sum += (nums[right] - nums[right - 1]) * (right - left)
            
            # If the total operations exceed k, shrink the window from the left
            while current_sum > k:
                current_sum -= nums[right] - nums[left]
                left += 1
            
            # Update the maximum frequency
            max_freq = max(max_freq, right - left + 1)
        
        return max_freq
