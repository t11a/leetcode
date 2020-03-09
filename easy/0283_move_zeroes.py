class Solution:
    def moveZeroes(self, nums):
        zero_cnt = 0

        # count
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zero_cnt += 1

        # delete 0 element
        while True:
            if 0 in nums:
                nums.remove(0)
            else:
                break

        # append 0 to nums
        for _ in range(0, zero_cnt):
            nums.append(0)



nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums == [1,3,12,0,0])