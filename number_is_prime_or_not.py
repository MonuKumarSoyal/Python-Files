number = int(input("Enter the number: \n"))
k = 0
for i in range(2,number):
    if number%i == 0:
        k = 1

if k == 0:
    print("Number",number,"is Prime Number")
else:
    print("Number",number,"is not a Prime Number")