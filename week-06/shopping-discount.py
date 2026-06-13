from discount import final_price, TAX_RATE

products = [
    ("Laptop", 85000, 10),
    ("Headphones", 4500, 15),
    ("Phone Case", 800, 5),
    ("USB Cable", 600, 0),
]

print(f"Tax Rate (VAT): {TAX_RATE * 100}%\n")
print("Shopping Discount Summary:")
print("-" * 57)
print(f"{'Product':<20} {'Original Price':<20} {'Final Price':<20}")
print("-" * 57)

for product_name, original_price, discount_percent in products:
    final = final_price(original_price, discount_percent)
    print(f"{product_name:<20} NPR {original_price:<18} NPR {final:.2f}")

print("-" * 57)
