class Solution:
    def twoSum(self, nums: List[int], target: int):
        n = len(nums)
        h = {}

        for i in range(n):
            comp = target - nums[i]
            if comp in h.keys():
                return [h[comp], i]
            h[nums[i]] = i

        return "No Combination"

print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([2,7,11,15], 100))