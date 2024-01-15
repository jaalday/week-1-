total_bill = float(input("Enter total "))
tip = 0
service = (input("Service? "))

if service == "good":
    tip = (total_bill * 0.2)
    
elif service == "fair":
    tip = (total_bill * 0.15)
    
elif service == "bad":
    tip = (total_bill * .10)
    
tip_amount = (tip)
print(tip_amount)

total_amount = (tip + total_bill)
print(total_amount)
    
    
    
    
  


    
    

# tipgood = float(total * 0.2)
# tipfair = float(total * 0.15)
# tipbad = float(total * 0.10)