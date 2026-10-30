
n = int(input("Enter number of locations: "))
minimum_stock = 20

for i in range(n):
    print("\nLocation", i + 1)
    name = input("Enter location name: ")
    received = int(input("Quantity received: "))
    distributed = int(input("Quantity distributed: "))
    damaged = int(input("Quantity damaged: "))
    remaining = int(input("Actual remaining stock: "))

    expected = received - distributed - damaged
    discrepancy = remaining - expected
    replenishment = max(0, minimum_stock - remaining)

    print("\n--- Stock Report ---")
    print("Location:", name)
    print("Expected Stock:", expected)
    print("Actual Stock:", remaining)
    print("Discrepancy:", discrepancy)
    print("Replenishment Required:", replenishment)

    if discrepancy == 0:
        print("Stock Status: Matched")
    else:
        print("Stock Status: Discrepancy Found")

print("\nStock Reconciliation Completed!")

