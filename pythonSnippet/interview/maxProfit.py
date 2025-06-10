def maxProfit(prices):
    profit = 0
    currentSmallestBuy = prices[0]
    i = 0
    while i < len(prices) - 1:
        if i == 0 or prices[i] < currentSmallestBuy:
            currentSmallestBuy = prices[i]
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    i = j
                    continue
                else:
                    profit = max(profit, prices[j] - prices[i])
        i += 1
    return profit

def maxProfit2(prices):
    profit = 0
    currentSmallestBuy = prices[0]
    for e in prices:
        if e < currentSmallestBuy:
            currentSmallestBuy = e
        else:
            profit = max(profit, e - currentSmallestBuy)
    return profit

stockPriceList = list(range(100000, 0, -1))
print(maxProfit(stockPriceList))