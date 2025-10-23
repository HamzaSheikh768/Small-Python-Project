# ================== Rent Calculator ==================
# input we need from the user
# Total food ordered for snacking
# Electricity bill
# Persons living in the house
# output
# Total amount you 've to pay

rent = int(input("Enter your house rent: "))
food = int(input("Enter the amount of house grocery: "))
electricity = int(input("Enter the electricity bill: "))
persons = int(input("Enter the number of persons living in the house: "))

total_amount = rent + food + electricity
output = (total_amount // persons)
print(f"The total amount you have to pay is per person: {output}")