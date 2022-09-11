# list = ["anil" , "soyal",]
# second_list = {'age' : 20, 'doy' : 2001, 'dom' : 9, 'dod' : 17 }


# def hello(*anil, **soyal):
#     print(anil)
#     print(soyal)

# # hello("anil", "soyal", age = 20, doy = 2001, dom = 9, dod = 17)
# hello(*list, **second_list)

# --------------------------------------------------------------------------------------------------

# list = []

# for i in range(0, 5):
#     list.append(int(input()))

# def summation_of_list_content(list):
#     y = 0
#     for x in list:
#         y += x
#     return y, y+5

# print(summation_of_list_content(list))

# ----------------------------------------------------------------------------------------------------------

# lambda function --> it is also called anonymous function(function with no name) 
# if we have a function with one line of code then we can write a lambda function equivalent to that funcion 

# def summation(a, b):
#     return a+b

# print(summation(5, 6))

# above is same as 


# addition = lambda a, b: a+b

# print(addition(4, 5))


# def even(num):
#     if num%2 == 0:
#         return True


# print(even(12))


# above function can be written as 

# even = lambda num: num%2 == 0
# print(even(6))

# -----------------------------------------------------------------------------------------------------------

# difference between map and filter 

# lst = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]    

# def even_or_odd(num):
#     if num%2 == 0:
#         print("The number {} is even".format(num))
#     else:
#         print("The number {} is odd".format(num))

# def even(num):
#     if num%2 == 0:
#         return True


# print(list(map(even, lst)))

# print(list(filter(even, lst)))

# map and filter function using lambda function 

# print(list(map(lambda num: num%2 == 0, lst))) 
# print(list(filter(lambda num: num%2 == 0, lst)))

# list comprehension 
 
# lst1 = []
# lst = [1, 2, 3, 4, 5, 6, 7]

# def square_list(lst):
#     for i in lst:
#        lst1.append(i*i) 


# square_list(lst)
# print(lst1)

# print([i*i for i in lst if i%2 != 0])


# String Formatting 

# If we want to write some part of the string as dynamically then we can use a function called format() in this we have to give the parameter for the placeholder

# def description(name, age):
#     print("My name is {} and age is {}".format(name, age))


# def description1(name, age):
#     print("My name is {name1} and age is {age1}".format(age1 = age, name1 = name)) # here name1 and age1 are temporary variables

# description("Monu", 20)
# description("Anil", 20)

# List Iterables and Irerators 

# The basic difference between the iteeables and iterators is that when we initilize the iterables(like list) then it gets stored in the memory but iterators don't get stored when we initilize it, it will only be initilized when we execute it using next function like below.

# we use the function iter() to convert a iterables into iterators 

# lst = [1, 2, 3, 4, 5, 6, 7]

# for i in lst:
#     print(i)

# lst1 = iter(lst)
# # lst1 = lst
# for i in lst1:
#     print(i)

# print(lst1[0])    # this will throw an error if we convert the iterable lst into iterator lst1





