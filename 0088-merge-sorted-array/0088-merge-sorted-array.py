class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Pointers for nums1, nums2, and the merged array
        nums1_index = m - 1  # Last valid element in nums1
        nums2_index = n - 1  # Last element in nums2
        merge_index = m + n - 1  # Last position in nums1

        # Merge nums1 and nums2 starting from the end
        while nums1_index >= 0 and nums2_index >= 0:
            if nums1[nums1_index] > nums2[nums2_index]:
                nums1[merge_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[merge_index] = nums2[nums2_index]
                nums2_index -= 1
            merge_index -= 1

        # If there are still elements in nums2, copy them
        while nums2_index >= 0:
            nums1[merge_index] = nums2[nums2_index]
            nums2_index -= 1
            merge_index -= 1
