# PROBLEM 19: Best Time to Buy and Sell Stock
# LeetCode 121
# Question: You are given an array prices where prices[i] is the price of a given stock on the i-th day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell it.
# Return the maximum profit you can achieve from this transaction. If no profit is possible, return 0.
# ============================================================

class Solution19:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]   # lowest buy price seen so far
        max_profit = 0
        print(f"Initial: min_price={min_price}, max_profit={max_profit}")

        for i, price in enumerate(prices[1:], start=1):
            profit = price - min_price          # profit if sold today
            print(f"Day {i}, Price={price}, Profit={profit}, min_price={min_price}")
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)   # update lowest price seen
            print(f"   Updated: max_profit={max_profit}, min_price={min_price}")

        print("Final max_profit =", max_profit)
        return max_profit

# Testing
sol = Solution19()
print("Answer:", sol.maxProfit([7,1,5,3,6,4]))   # Expected 5 (buy at 1, sell at 6)
print("Answer:", sol.maxProfit([7,6,4,3,1]))     # Expected 0 (no profit possible)
