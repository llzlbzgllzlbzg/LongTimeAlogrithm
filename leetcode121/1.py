from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]
        for price in prices:
            ans = max(ans, price - min_price)
            min_price = min(min_price, price)
        return ans