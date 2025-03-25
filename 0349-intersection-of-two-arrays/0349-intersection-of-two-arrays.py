class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # freq1 = {}
        # # freq2 = {}
        # arr = []
        # for num in nums1:
        #     freq1[num] = freq1.get(num,0) + 1
        
        # # for num in nums2:
        #     # freq2[num] = freq2.get(num,0) + 1
        
        # for num in nums2:
        #     if num in freq1:
        #         arr.append(num)
        #         del freq1[num]
        # return arr

        hash_set = set(nums1)
        result = set()

        for num in nums2:
            if num in hash_set:
                result.add(num)
        
        return list(result)



        