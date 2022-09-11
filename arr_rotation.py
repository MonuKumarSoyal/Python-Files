arr = []
length_of_arr = int(input("Enter the length of arr:\n"))
# print("Enter the values in the arr:")
for i in range(1, length_of_arr+1):
    # a = int(input())
    # arr.append(a)
    arr.append(i)

print("Enter the rotation value:")
rotation_value = int(input())

for j in range(0,rotation_value):
    b = arr.pop(0)
    arr.append(b)

print(arr)

