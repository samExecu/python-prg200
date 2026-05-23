#dummy stock
inventory = [
    {"item": "Rice", "stock": 5, "threshold": 10},
    {"item": "Eggs", "stock": 24, "threshold": 12},
    {"item": "Milk", "stock": 3, "threshold": 6},
    {"item": "Bread", "stock": 8, "threshold": 5},
    {"item": "Chicken", "stock": 0, "threshold": 4},
    {"item": "Cooking Oil", "stock": 2, "threshold": 3},
]

#creating a empty list to add the names of items that are low in stock
restocking = []

#compares the threshold and stock value of each item, and if stock is low then add the item name to restocking list
for item in inventory:
  if(item["stock"] < item["threshold"]): restocking.append(item["item"])

#printing items that are low in stock
print(f"Low in Stock: {len(restocking)} items")
for i, item in enumerate(restocking):
  print(f"Item {i+1}: {item}")
