
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ### A TRY..(tried it)
        '''buy,sold=float('inf'),-float('inf')
        for i in range(0,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            elif sold<prices[i]:
                sold=prices[i]
        return sold-buy'''
        max_profit=0
        buy=prices[0]
        for i in range(0,len(prices)):  
            if buy>prices[i]: #meaning - found a cheaper price thaan before
                buy=prices[i]
            else:
                max_profit=max(max_profit,prices[i]-buy)
        return max_profit



        
