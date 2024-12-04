item_prices={"shirt":300, "tshirt":200, "jeans":500}

discounted_prices={item:price *0.9 for item,price in item_prices.items()}

print("prices after 10% discount:",discounted_prices)