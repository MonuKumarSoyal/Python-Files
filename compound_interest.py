amount = float(input("Enter the Amount: \n"))
rate = float(input("Enter the Rate: \n"))
time = float(input("Enter the Time: \n"))

Total_amount = amount*(pow((1+ (rate)/100), time))
interest = Total_amount - amount
print("The Total amount is :", Total_amount)
print("The Interest is :", interest)