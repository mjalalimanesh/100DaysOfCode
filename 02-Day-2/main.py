""" Split the bill considering percentage of the tip """

print("Welcome to the tip calculator.")

bill_amount = float(input("What was the total bill? "))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

total_amount = bill_amount + (percentage_tip / 100) * bill_amount
share_of_each_person = round(total_amount / number_of_people, 2)

print(f"Each person should pay: ${share_of_each_person}")
