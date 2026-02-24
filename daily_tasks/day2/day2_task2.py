total_bill_amount = float(input("Enter the total bill amount: "))
num_of_people = int(input("Enter the number of people: "))
share_per_person = total_bill_amount / num_of_people
print( f"Total Bill: {total_bill_amount}, Each person pays: {share_per_person}" )