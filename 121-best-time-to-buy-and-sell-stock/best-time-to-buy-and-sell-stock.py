class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cheap_price = prices[0]
        max_profit = 0
        for i in prices[1:]:
            if i<=cheap_price:
                cheap_price=i
                print(cheap_price,max_profit)
            else:
                max_profit = (i - cheap_price) if (i - cheap_price) > max_profit else max_profit
                print(i,cheap_price,max_profit)
        return max_profit
            
        
        
            