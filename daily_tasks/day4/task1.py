contacts = {
    'Alice': '123-456-7890',
    'Bob': '987-654-3210',
    'Charlie': '555-555-5555'}
print(contacts)

#ADD and Update the contacts

contacts['Alice'] = '999-888-7777'

print("Updated Contacts:", contacts)

#get() method

print("Bob's contact number is:", contacts.get('Bob', 'Not Found'))
print("David's contact number is:", contacts.get('David', 'Not Found'))

for name, number in contacts.items():
    print(f"{name}: {number}")
