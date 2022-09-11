arr = []
length_of_arr = int(input("Enter the length of the arr: \n"))
print("Enter the values in arr:")
for i in range(1, length_of_arr+1):
    a = int(input())
    arr.append(a)

element = arr[0]
for j in range(1, length_of_arr):    
    if element<arr[j]:
        element = arr[j]

print("The greatest number is :", element)