arr = []
length_of_arr = int(input("Enter the length of arr:\n"))
print("Enter the number in arr: ")

for i in range(1, length_of_arr+1):
    a = int(input())
    arr.append(a)
sum = 0
for j in range(0,length_of_arr):
    sum = sum + arr[j]
    if j == (length_of_arr-1):
        print("The sum of elements is:",sum)