
n = int(input("Enter number of chemicals: "))

chemicals = []
invalid = False

for i in range(n):
    name = input("\nChemical name: ")
    category = input("Category (Acid/Base/Flammable/Oxidizer): ")
    quantity = float(input("Quantity in litres: "))

    chemicals.append([name, category, quantity])

    if category not in ["Acid", "Base", "Flammable", "Oxidizer"]:
        print("Invalid storage category!")
        invalid = True

    if quantity <= 0 or quantity > 50:
        print("Invalid quantity!")
        invalid = True

# Check compatibility
for i in range(n):
    for j in range(i + 1, n):
        c1 = chemicals[i][1]
        c2 = chemicals[j][1]

        if (c1 == "Acid" and c2 == "Base") or \
           (c1 == "Base" and c2 == "Acid") or \
           (c1 == "Flammable" and c2 == "Oxidizer") or \
           (c1 == "Oxidizer" and c2 == "Flammable"):

            print("Incompatible:", chemicals[i][0],
                  "and", chemicals[j][0])
            invalid = True

if invalid:
    print("\nInventory contains invalid records!")
else:
    print("\nAll inventory records are valid.")

