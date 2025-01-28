#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
tip_per = tip/100
tot_tip = bill*tip_per
total_bill = bill + tot_tip
bill_per_person = total_bill/split
final_amt=round(bill_per_person,2)
print(f"Each person should pay: ${final_amt}")
