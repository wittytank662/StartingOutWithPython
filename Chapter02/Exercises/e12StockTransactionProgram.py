shares = 2000
initPrice = 40.00
stockBrokerBuyCommission = (initPrice * shares) * 0.03 #3% of the aomunt paid for the stock

# Two weeks later

sharesSold = 2000
soldPrice = 42.75
stockBrokerSellCommission = (soldPrice * sharesSold) * 0.03 #3% of the amount he recieved

print(f"Joe paid ${(initPrice * shares):,}, for the stock, he paid his broker ${(stockBrokerBuyCommission):,}, Joe sold the stock for ${(soldPrice * sharesSold):,}.")
print(f"Joe's broker was commissioned ${stockBrokerSellCommission:,}.")
print()
print(f"After selling the stock Joe made ${(((soldPrice * sharesSold) - (initPrice * shares)) - (stockBrokerBuyCommission + stockBrokerSellCommission)):,}.")