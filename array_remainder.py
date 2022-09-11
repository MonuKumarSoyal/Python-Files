arr = []
n = int(input("Enter the value of divider :\n"))
length_of_arr = int(input("Enter the length of the array:\n"))
print("Enter the elements in the array: ")
for i in range(0, length_of_arr):
    a = int(input())
    arr.append(a)
    

multiplication = 1

for i in range(0, length_of_arr):
    multiplication = multiplication*arr[i]

print("The remainder is :", multiplication%n)