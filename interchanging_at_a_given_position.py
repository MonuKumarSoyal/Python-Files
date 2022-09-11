list = []
size_of_list = int(input("Enter the size of the list: \n"))

for i in range(0, size_of_list):
    a = input()
    list.append(a)

print("Your entered values in the list:")

for i in range(0, size_of_list):
    print(list[i], end = " ")

anil = int(input("\nEnter the first position:"))
monu = int(input("Enter the second position:"))
anil -= 1
monu -= 1
list[anil], list[monu] = list[monu], list[anil]

print("New list with interchanging the numbers at the given position: ")


for i in range(0, size_of_list):
    print(list[i], end = " ")
