name=input("Enter your name: ")
age=int(input("Enter your age: "))
age_in_2030= age+4
print("Your age in 2030 will be:", age_in_2030)
print("\n")

total_bill_amount = float(input("Enter the total bill amount: "))
num_of_people = int(input("Enter the number of people: "))
share_per_person = total_bill_amount / num_of_people
print( f"Total Bill: {total_bill_amount}, Each person pays: {share_per_person}" )
print("\n")

item_name="Watch"
quantity=2
price= 1300
in_stock=True
total_cost= quantity * price
print("Item:", item_name, " Quantity:", quantity, " Price:", price, " Available:", in_stock)
print("Total Cost:", total_cost)