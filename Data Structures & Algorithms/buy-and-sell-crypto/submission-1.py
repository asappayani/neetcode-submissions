class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        sliding window

        increase window size, check what the profit would be. our left is the day we buy, and
        the right is the day we sell.

        prices = [10,1,5,6,7,1]
        """
        ans = 0
        left = 0
        right = 1

        while right < len(prices):
            profit = prices[right] - prices[left]

            if profit > 0:
                ans = max(profit, ans)
            else:
                left = right

            right += 1
                
        return ans



