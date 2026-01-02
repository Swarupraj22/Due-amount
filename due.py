def calculate_return(total_bill, amount_paid):
    return amount_paid - total_bill

total_bill = float(input("Enter the total bill of the item: "))
amount_paid = float(input("Enter the amount you paid: "))

return_amount = calculate_return(total_bill, amount_paid)

if amount_paid > total_bill:
    print("The shopkeeper should return:", return_amount, "Rs")
elif amount_paid < total_bill:
    print("You should return to shopkeeper:", abs(return_amount), "Rs")

