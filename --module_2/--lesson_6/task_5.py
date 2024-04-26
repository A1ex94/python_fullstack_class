price = [5, 10, 15, 25, 20]   

min_price = price.index(min(price))
high_price = price.index(max(price))

price[min_price], price[high_price] = max(price), min(price)

print(price)