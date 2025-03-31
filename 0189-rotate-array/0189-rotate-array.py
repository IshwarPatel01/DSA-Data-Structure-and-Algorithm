class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        temp = [0] * n

        for i in range(n):
            new_index = (i + k) % n
            temp[new_index] = nums[i]

        nums[:] = temp


                    


        

        """
        Do not return anything, modify nums in-place instead.
        """
        