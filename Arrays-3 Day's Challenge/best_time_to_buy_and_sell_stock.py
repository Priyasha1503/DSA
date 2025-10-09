#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=float('inf')
        max_profit=0
        for i in range(0,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            else:
                #sold_max=max(sold_max,prices[i])
                sold=prices[i] 
                max_profit=max(max_profit,sold-buy)
        return max_profit
 
