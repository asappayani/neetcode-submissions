class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        sliding window

        increase window size, check what the profit would be. our left is the day we buy, and
        the right is the day we sell.

        prices = [10,1,5,6,7,1]
        """
        ans = 0

        for left in range(len(prices)):
            right = left
            profit = prices[right] - prices[left]

            while right < len(prices) and profit >= 0:
                ans = max(ans, profit)
                right += 1

                if right < len(prices):
                    profit = prices[right] - prices[left]

                

        return ans



