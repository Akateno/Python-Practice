print("Welcome to the tip calculator")
#remember the input will come in as a string so you have to convert to an integer, check with type(total)
total = float(input("what was your total bill? $"))
#once again we convert to integer 
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

people = int(input("how many poeople are splitting the bill?"))

tip_as_percent = tip/100
total_tip_amount = total * tip_as_percent
total_bill = total + total_tip_amount
bill_per_person = total_bill / people 
final_amount = round(bill_per_person, 2)
final_amount = "{:.f}".format(bill_per_person)

print(f"Each Person should pay ${final_amount}")


