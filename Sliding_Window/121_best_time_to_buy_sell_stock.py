from typing import List

# Time complexity: O(n^2) ==> time limit exceeds
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = -2**31 -1
#         for b in range(len(prices)):
#             for s in range(b + 1, len(prices)):
#                 profit = prices[s] - prices[b]
#                 max_profit = max(max_profit, profit)
#         if max_profit < 0:
#             return 0
#         else:
#             return max_profit


class Solution:
    '''
    At first, we buy stock. From second day, either we buy stock at lower price or determine profit.
    Gradually, we get minimum buy price and maximum profit
    '''
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for b in range(1, len(prices)):
            if prices[b] <= buy_price:
                buy_price = prices[b]
            else:
                profit = prices[b] - buy_price
                max_profit = max(max_profit, profit)



        return max_profit



sol = Solution()
print(sol.maxProfit(prices = [7,1,5,3,6,4]))
print(sol.maxProfit(prices = [7,6,4,3,1]))
