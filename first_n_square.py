from numpy import square


n = int(input("Enter the number:\n"))
sum = 0 # to store the sum of square 
sum1 = 0 # to store the sum of cube
for i in range(1, n+1):
    sum = sum + pow(i,2)
    sum1 = sum1 + pow(i,3)
    
print("The summation from 1 to",n,"is",sum)
print("The summation from 1 to",n,"is",sum1)