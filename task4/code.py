

products = {
    "Laptop": [50000, 10],
    "Mobile": [20000, 15],
    "Headphones": [2000, 20]
}

revenue = 0
dispatched = 0
returned = 0
orders = []

print("===== PRODUCT INVENTORY =====")
for name, details in products.items():
    print(name, "Price:", details[0],
          "Stock:", details[1])

n = int(input("\nEnter Number of Orders: "))

for i in range(n):
    print("\nOrder", i + 1)
    name = input("Enter Product Name: ")

    if name in products:
        qty = int(input("Enter Quantity: "))
        price, stock = products[name]

        if 0 < qty <= stock:
            amount = qty * price

            if amount >= 5000:
                discount = amount * 0.10
            else:
                discount = 0

            final_amount = amount - discount
            products[name][1] -= qty
            dispatched += qty
            revenue += final_amount

            print("Order Dispatched Successfully!")
            print("Discount:", discount)
            print("Order Amount:", final_amount)

            r = int(input("Enter Returned Quantity: "))

            if 0 <= r <= qty:
                products[name][1] += r
                returned += r
                revenue -= r * (final_amount / qty)
                orders.append([name, qty, r, final_amount])
            else:
                print("Invalid Return Quantity!")

        else:
            print("Insufficient Stock or Invalid Quantity!")

    else:
        print("Product Not Found!")

# Inventory reconciliation
print("\n===== FINAL INVENTORY REPORT =====")

for name, details in products.items():
    price, stock = details
    print(name, "Remaining Stock:", stock)

    if stock < 0:
        print("Stock Discrepancy Detected!")

print("\n===== SALES SUMMARY =====")
print("Total Orders:", len(orders))
print("Total Dispatched:", dispatched)
print("Total Returned:", returned)
print("Total Revenue: Rs.", round(revenue, 2))

print("\n===== ORDER DETAILS =====")
for order in orders:
    print("Product:", order[0],
          "Ordered:", order[1],
          "Returned:", order[2])

print("\nE-Commerce Reconciliation Completed!")

