print("Welcome to Tip calculator")

total_bill = float(input("What was the total bill? "))
tip = int(input("How much tip you want to give? 10, 12 or 15? "))
n_people = int(input("How many people to split the bill? "))

pay = (total_bill / n_people) * (1 + tip / 100)

print(f"Each person should pay: ${round(pay,2)}")
