def calculate_return(total_bill, amount_paid):
    return amount_paid - total_bill

total_bill = float(input("Enter the total bill of the item:"))
amount_paid = float(input("Enter the paid bill of the item:"))

return_amount = calculate_return(total_bill, amount_paid)

if total_bill<amount_paid:
    print("The shopkeeper should return:", return_amount, "Rs") 
else:
    print("You should return to shopkeeper:", abs(return_amount), "Rs") 