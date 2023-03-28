print("Welcome to bill calculator!!")
bill_price = float(input("Enter the value of the bill: "))
quantity_persons = int(input("Enter the quantity of persons: "))
price_per_person = bill_price/quantity_persons
print(f"Without taxes: Each person needs to pay: {price_per_person:.2f}")
print(f"With taxes: Each person needs to pay: {price_per_person*1.1:.2f}")
