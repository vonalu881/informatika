def best_deal(prices):
    if not prices or len(prices) < 2:
        return 0
        
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit
                
    return max_profit
