# You have a list of stock prices — one price per day. You can buy on one day and sell on a later day. 
# Find the maximum profit you can make. If you can't make profit, return 0.
# prices = [7, 1, 5, 3, 6, 4] Buy on day 2 (price=1), sell on day 5 (price=6) Profit = 6 - 1 = 5 → Answer: 5 
# prices = [7, 6, 4, 3, 1] Prices only go down — no profit possible → Answer: 0


def maxprofit(prices):
    min_price =float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
print(maxprofit([7,1,5,3,6,4]))
print(maxprofit([3,4,1,6,8]))
