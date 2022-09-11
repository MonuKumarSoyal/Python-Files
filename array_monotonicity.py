arr = []
size_of_arr = int(input("Enter the size of the arr: \n"))

for i in range(0, size_of_arr):
    a = int(input())
    arr.append(a)

anil = 0
monu = 0
ravi = 0



if arr[0] > arr[1]:
     for i in range(1, (size_of_arr-1)):
         if arr[i] > arr[i+1]:
             monu += 1

elif arr[0] < arr[1]:
     for i in range(1, (size_of_arr-1)):
         if arr[i] < arr[i+1]:
             anil += 1
             

elif arr[0] == arr[1]:
     for i in range(1, (size_of_arr-1)):
         if arr[i] == arr[i+1]:
             ravi += 1

if anil == (size_of_arr-2) or monu == (size_of_arr-2) or ravi == (size_of_arr-2):
    print("True")
else:
    print("False")
