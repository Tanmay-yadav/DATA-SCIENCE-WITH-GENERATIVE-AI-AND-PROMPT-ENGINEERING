# # _______________________function_____________________________
# 
# # A function in programming is a block of code 
# # designed to perform a specific task. It is a 
# # reusable piece of code that can be called from 
# # different parts of a program. Functions help in 
# # organizing code, making it more modular, readable, 
# # and maintainable.
# # ............................................................
# # __________________________TYPES OF FUNCTION_________________
# # 1.inbult or builtin or pre-defined(print,append,len,list,etc)
# # 2.user defined function{
# # i.defining  function>>>>def functionname():
# # #                           //body of the function//
# #                             //return output//
# # ii.calling function>>>>by functionname()}
# # ............................................................

# # function for adding two numbers
# # defination
# def add_two(num1,num2):
#     output= num1 + num2
#     return output #..........exit or terminate the function and return the value
# #    ek function mein ek se jaada return value 
# # ho sakti hai lekin use ek hi hoga jo first hoga
# # ............................................................
# a=int(input("enter number1:"))
# b=int(input("enter number2:"))
# # calling output
# # output = add_two(num1=a,num2=b)#output likna jaroori hai kyuki return waala output 
# # show nahi karega
# output=add_two(a,b)#positional arguments<a and b>
# print("your addition is:",output)# agar hum printuse nahi karenge to yeh output show nahi karege
# output=len(ls)
# print(output)
# # print(len(ls))
# ................................................................
# _________________making length function by overself_____________
# ................................................................
# def my_len(list):
#     count=0
#     for item in list:
#         count+=1
#     # return count
# ////////////////////////////////////////////////////
# def my_len(list):
#     count=0
#     for item in list:
#         count+=item
#     return count

# marks=[41,52,23,23,56,7,8,66,99,1099]
# print(my_len(list=marks))

#  output = my_len(list) this is wrong errot: type
# print(my_len(marks))
# ........................................................................
# _______________________ASSINGMENT FOR TODAY___________________________________
# .............................................................................
# 1.average_finder()
#2. even_finder()
# 3.average_finder_even()
# 4.my_min()
# 5.my_max()
#.............................................................................
#_____________________________________MODULE___________________________________
#Module: A module in Python is a file that contains Python definitions and statements
# . Modules can define functions, classes, and variables, as well as include runnable code. 
# The file name is the module name with the suffix .py added.
# Modules allow you to logically organize your Python code into separate files, 
# which makes it easier to maintain and reuse. They can be imported into other modules or scripts, 
# allowing you to use the functions, classes, and variables defined in them.
# .....................................................................................
