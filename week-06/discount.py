# Discount module for shopping application
TAX_RATE = 0.13  # global constant (13% VAT)

def apply_discount(price, percent):
    # Calculates the price after discount and returns it
    discount_amount = price * (percent / 100)
    return price - discount_amount

def apply_tax(price):
    # Calculates the price after adding the Tax and returns it
    tax_amount = price * TAX_RATE
    return price + tax_amount

def final_price(price, discount_pct):
    # Caclulates the final amount by first applying the discount and then adding the Tax amount
    discounted_price = apply_discount(price, discount_pct)
    final = apply_tax(discounted_price)
    return final
