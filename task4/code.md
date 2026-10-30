

## 1. Problem Statement

Develop a Python program to manage an integrated E-Commerce Order Processing and Reconciliation System. The program should process customer product orders, calculate discounts, manage product dispatches, process product returns, and update available stock.

The program should calculate total sales revenue after discounts and returns, identify stock discrepancies between available and expected inventory, and generate a final inventory summary.

The program should use variables, conditional statements, loops, lists, dictionaries, and arithmetic operators to manage orders and inventory efficiently.

## 2. Algorithm

1. Start the program.
2. Initialize product details with product names, prices, and available stock.
3. Display the product list.
4. Enter the number of orders.
5. For each order:
   - Enter product name.
   - Enter order quantity.
   - Check product availability.
   - Calculate the total order amount.
   - Apply a discount if the order amount is ₹5,000 or more.
   - Calculate the final order amount.
6. Process dispatch:
   - Reduce the stock according to the dispatched quantity.
   - Calculate the total dispatched quantity.
7. Process product returns:
   - Enter the returned quantity.
   - Add returned products back to stock.
   - Subtract the returned amount from revenue.
8. Calculate total revenue after discounts and returns.
9. Compare expected stock with actual stock.
10. Identify inventory discrepancies.
11. Display the final sales and inventory report.
12. Stop the program.


## 3. Flowchart 
```mermaid code


## 4. Sample Input

```
===== PRODUCT INVENTORY =====
Laptop Price: 50000 Stock: 10
Mobile Price: 20000 Stock: 15
Headphones Price: 2000 Stock: 20

Enter Number of Orders: 2

Order 1
Enter Product Name: Laptop
Enter Quantity: 2
Enter Returned Quantity: 1

Order 2
Enter Product Name: Mobile
Enter Quantity: 2
Enter Returned Quantity: 0
```

## 5. Sample Output

```
===== PRODUCT INVENTORY =====
Laptop Price: 50000 Stock: 10
Mobile Price: 20000 Stock: 15
Headphones Price: 2000 Stock: 20

Order 1
Order Dispatched Successfully!
Discount: 10000.0
Order Amount: 90000.0

Order 2
Order Dispatched Successfully!
Discount: 4000.0
Order Amount: 36000.0

===== FINAL INVENTORY REPORT =====
Laptop Remaining Stock: 9
Mobile Remaining Stock: 13
Headphones Remaining Stock: 20

===== SALES SUMMARY =====
Total Orders: 2
Total Dispatched: 4
Total Returned: 1
Total Revenue: Rs. 81000.0

===== ORDER DETAILS =====
Product: Laptop Ordered: 2 Returned: 1
Product: Mobile Ordered: 2 Returned: 0

E-Commerce Reconciliation Completed!
```

