from cmath import sqrt

from numpy import integer


number = int(input("Enter the number : \n"))

value1 = 5*(pow(number,2)) + 4
value2 = 5*(pow(number,2)) - 4

a = sqrt(value1)
b = sqrt(value2)
if isinstance(a,int) | isinstance(b,int):
    print("YES")
else:
    print("NO")

