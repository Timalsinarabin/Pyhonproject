items = []
prices = []
total = 0

def ui():
    print("-"*30)

while True:
    item=input("Enter name of the product (q for quit): ")
    if item.lower() == 'q':
        break
    else:
        items.append(item)
        try:
            p = float(input(f"Enter price of {item}: Rs "))
            prices.append(p)
        except ValueError:
            print("Invalid price. Please input valid numerical value.")

print(f"{'-'*8} Shoping Cart {'-'*8}")
print(" Item"+" "*15+"Price")
ui()

for item,price in zip(items,prices):
    print(f" {item:<15} Rs {price:>7.2f}")

for p in prices:
    total += p
ui()
print(f" {'Total':<15} Rs {total:>7.2f}")
