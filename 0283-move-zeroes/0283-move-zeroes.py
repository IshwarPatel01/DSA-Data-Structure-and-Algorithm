class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        count = 0
        j = 0
        # temp = nums[0]
        for i in range(n):
            if nums[i] != 0:
                nums[i - j] = nums[i]
            else:
                count += 1
                j += 1
        for i in range(n-j,n):
            nums[i] = 0
        return nums





