'''Problem : Best Time to Buy and Sell Stock
Platform: LeetCode 121
Question: 
You are given an array prices where prices[i] is the price of a stock on day i. Find the maximum profit you can achieve by buying and selling once.
Approach:
Track the minimum buying price seen so far.
Calculate profit daily as current_price - min_price.
Update maximum profit.
Time Complexity: O(n).'''

def maxProfit(prices):
    mini = prices[0]
    profit = 0
    for p in prices:
        mini = min(mini, p)
        profit = max(profit, p - mini)
    return profit

print(maxProfit([7,1,5,3,6,4]))  # 5
