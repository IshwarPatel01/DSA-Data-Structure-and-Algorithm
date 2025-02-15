class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        
         
   




















































        # midx = m - 1
        # nidx = n - 1 
        # right = m + n - 1

        # while nidx >= 0:
        #     if midx >= 0 and nums1[midx] > nums2[nidx]:
        #         nums1[right] = nums1[midx]
        #         midx -= 1
        #     else:
        #         nums1[right] = nums2[nidx]
        #         nidx -= 1

        #     right -= 1