class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero_num = 0

        for i in range(n):
            if nums[i] == 0:
                zero_num += 1

        ans = []
        for i in range(n):
            if nums[i] != 0:
                ans.append(nums[i])

        for i in range(zero_num):
            ans.append(0)

        for i in range(n):
            nums[i] = ans[i]

nums=[0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums == [1,3,12,0,0])
