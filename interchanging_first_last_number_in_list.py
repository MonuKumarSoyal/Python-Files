list = []
size_of_list = int(input("Enter the size of the list: \n"))

for i in range(0, size_of_list):
    a = input()
    list.append(a)

print("Your entered values in the list:")

for i in range(0, size_of_list):
    print(list[i], end = " ")

list[0], list[size_of_list-1] = list[size_of_list-1], list[0]

print("\nNew list with interchanging of the first and last number: ")


for i in range(0, size_of_list):
    print(list[i], end = " ")
