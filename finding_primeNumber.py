x = int(input("Enter the left number:\n"))
z = int(input("Enter the right number:\n"))
y = z+1
l = 0
for i in range(x,y):
    k = 0
    for j in range(2, i):
      if i%j ==0:
          k = 1
          continue
    if k == 0:
        print(i,end = " ")
        l = 1
if l == 0: 
    print("All Numbers are prime")