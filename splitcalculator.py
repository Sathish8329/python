print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

percentage = tip / 100 * total + total

total_per_person = percentage / people

final_amount = round(total_per_person, 2)

print(final_amount)
