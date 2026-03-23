'''Same as Day 1 stock BUT now you can buy and sell as many times as you want. 
Find maximum total profit.
prices = [7,1,5,3,6,4] → 7 (buy@1 sell@5=4, buy@3 sell@6=3) 
prices = [1,2,3,4,5] → 4 (buy@1 sell@5) prices = [7,6,4,3,1] → 0 (prices only fall)'''

def buy_sell_2(prices):                           # [5,8,6,2]
    profit = 0                                    # profit = 0
    for i in range(1,len(prices)):                # i=0,(0,4)
        if prices[i] > prices[i-1]:               # 5 > 0
            profit += prices[i] - prices[i-1]     # 0=0+5-0
    return profit                                 # 5

print(buy_sell_2([5,8,6,2]))
print(buy_sell_2([7,1,5,3,6,4]))  
print(buy_sell_2([1,2,3,4,5]))     
print(buy_sell_2([7,6,4,3,1]))  