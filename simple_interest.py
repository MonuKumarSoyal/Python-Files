amount = int(input("Enter the Amount: \n"))
time = int(input("Enter the Time: \n"))
rate = int(input("Enter the Rate: \n"))

interest = (amount*time*rate)/100
total_amount = interest + amount
print("The Interest is :",interest)
print("The Total Amount is :", total_amount)