class Solution(object):
    def maxProfit(self, prices):
        buying = 0
        selling = 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[buying]:
                buying = i
            elif prices[i] - prices[buying] > max_profit:
                selling = i
                max_profit = prices[selling] - prices[buying]
        # return max_profit if max_profit > 0 else 0
        return max(max_profit, 0)
        