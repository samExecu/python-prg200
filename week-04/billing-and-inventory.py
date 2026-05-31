# dummy data
inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}

cart = {"rice": 2, "milk": 3, "eggs": 12}

def process_order(inventory, cart):
  print("---- Bill ----")
  total = 0

  # Going through each of the item in the cart
  for item in cart:
    if item in inventory:
      if inventory[item]['stock'] >= cart[item]:
        cost = inventory[item]['price'] * cart[item]
        total += cost

        #Updating the stock
        inventory[item]['stock'] -= cart[item]
        # Print item bill
        print(f"{item} x{cart[item]} = NPR {cost}")
      else:
        #if carts item quantity is greater than stock quantity
        print(f"Sorry, not enough stock for {item}")
    else:
      #if there isn't any stock left of that item in the inventory
      print(f"{item} is not available in inventory")

  #Showing the total amount
  print(f"Grand Total: NPR {total}")
  print("--------------")

  #Displaying the updated stock
  updated_stock = []
  for item in cart:
    updated_stock.append(f"{item}={inventory[item]['stock']}")

  print("Updated stock: " + ", ".join(updated_stock))

process_order(inventory, cart)
