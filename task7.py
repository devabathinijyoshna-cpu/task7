n = int(input("Enter number of products: "))

total = 0

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    total = total + amount

if total >= 5000:
    discount = total * 0.10
elif total >= 2000:
    discount = total * 0.05
else:
    discount = 0

tax = (total - discount) * 0.05
final_bill = total - discount + tax

print("Total Amount:", total)
print("Discount:", discount)
print("Tax:", tax)
print("Final Bill:", final_bill)