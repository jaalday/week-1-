total_bill = float(input("Enter total "))
people = int(input("how many people? "))
tip = 0

service = (input("service? "))

if service == "good":
    tip = (total_bill * 0.2)
    
if service == "fair":
    tip = (total_bill * 0.15)
    
if service == "bad":
    tip = (total_bill * .10)
    
total_amount = float(tip + total_bill)
print(total_amount)

total_split = float(tip + total_bill/people)
print("each pay ", total_split )
    
