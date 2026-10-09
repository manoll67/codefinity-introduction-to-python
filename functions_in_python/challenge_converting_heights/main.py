# Given tuple of prices
prices = (12.3456, 49.987, 7.432, 99.999, 25.678, 40.123, 8.765, 71.333, 15.25, 3.1415, 89.654, 55.789, 60.432, 23.876, 19.99)

# Lists to store results
final_prices = []
rounded_prices = []

# Write your code here
for price in prices:
    final_prices.append(round(price,2)) # Rounding to two decimal places
    rounded_prices.append(round(price))# Rounding to the nearest whole number

# Testing results
print("Final Prices (rounded to 2 decimals):", final_prices)
print("Rounded Prices (nearest whole number):", rounded_prices)