
# Retail Billing with Multiple Discount Rules

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

print("\nEnter Product Details")

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category: ").lower()
    price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity

    # Category-specific tax
    if category == "electronics":
        tax_rate = 18
    elif category == "clothing":
        tax_rate = 5
    elif category == "groceries":
        tax_rate = 2
    else:
        tax_rate = 0

    tax = amount * tax_rate / 100

    subtotal += amount
    total_tax += tax

    print("\nProduct:", name)
    print("Amount: Rs.", round(amount, 2))
    print("Tax:", tax_rate, "%")
    print("Tax Amount: Rs.", round(tax, 2))

# Calculate total before discount
total = subtotal + total_tax

# Discount rules
if total >= 10000:
    discount_rate = 15
elif total >= 5000:
    discount_rate = 10
elif total >= 1000:
    discount_rate = 5
else:
    discount_rate = 0

discount = total * discount_rate / 100

# Maximum concession limit
max_discount = 1500
if discount > max_discount:
    discount = max_discount

# Final bill amount
final_amount = total - discount

# Display invoice
print("\n========== RETAIL INVOICE ==========")
print("Subtotal          : Rs.", round(subtotal, 2))
print("Total Tax         : Rs.", round(total_tax, 2))
print("Total Before Discount:", round(total, 2))
print("Discount Rate     :", discount_rate, "%")
print("Discount Amount   : Rs.", round(discount, 2))
print("------------------------------------")
print("Final Payable     : Rs.", round(final_amount, 2))
print("====================================")


