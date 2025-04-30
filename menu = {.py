menu = {
  'rice': 30,
  'pasta': 40,
  'burger': 60,
  'salad': 70,
  'coke': 15,
}

print("Welcome to Fahmida's Restaurant")
print("\n")
print("rice: 30 TK\nPasta: 40 TK\nBurger: 60 TK\nsalad: 70 Tk\nCoke: 30 TK")

order_total = 0

while True:
  item = input("Enter the item you want to order: ")
  item = item.lower()
  if item in menu:
      order_total += menu[item]
      print(f"Your item {item} has been added to your order")
  else:
      print("Sorry, we don't have that item on the menu")

  another_order = input("Do you want to add another item? (yes/no): ")
  if another_order.lower() != 'yes':
      break

print(f"The total amount to pay is {order_total} TK")


