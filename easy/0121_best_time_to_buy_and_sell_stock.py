class Solution:
    def maxProfit(self, prices):
        min_price = 10000
        max_prof = 0

        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif (prices[i] - min_price > max_prof):
                max_prof = prices[i] - min_price

        return max_prof

print(Solution().maxProfit([7,1,5,3,6,4])) # 5
print(Solution().maxProfit([7,6,4,3,1])) # 0