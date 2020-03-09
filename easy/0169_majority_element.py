class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        h = {}
        for i in nums:
            h[i] = h.get(i, 0) + 1

        for k,v in h.items():
            if v > (n/2):
                return k
        return None


print(Solution().majorityElement([3,2,3]) == 3)
print(Solution().majorityElement([2,2,1,1,1,2,2]) == 2)