number = input("Enter the number: \n")
length_of_number = len(number)
n = int(length_of_number)
Number = int(number)
armstrong = 0
for i in range(0,n):
    armstrong = armstrong + pow(int(number[i]),n)
if armstrong == Number:
    print("Yes")
else:
    print("No")
