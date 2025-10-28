# Name: Ben Ott
# Date: September 7th 2025
# Desciption: To calculate discount given for merchandise
# Hours invested: 0.5


merchandise = float(input("Enter the amount of merchandise: "))
print()
print("Calculating the discount.....")
print()

discount = 0

if merchandise >= 500:
    discount = 0.4
elif 200 <= merchandise < 500:
    discount = 0.2
else:
    discount = 0.1
    
total = merchandise - (merchandise * discount)

print(f"*****Amount payable is: {total:.2f}")
print()