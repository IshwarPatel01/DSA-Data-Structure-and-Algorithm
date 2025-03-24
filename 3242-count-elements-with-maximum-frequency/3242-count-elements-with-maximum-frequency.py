class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        hash_map = {}
        max_freq = 0
        for i in nums:
            hash_map[i] = hash_map.get(i,0) + 1
            if hash_map[i] > max_freq:
                max_freq = hash_map[i]
        
        total = 0

        for count in hash_map.values():
            if count == max_freq:
                total += max_freq
        
        return total

            

        
        