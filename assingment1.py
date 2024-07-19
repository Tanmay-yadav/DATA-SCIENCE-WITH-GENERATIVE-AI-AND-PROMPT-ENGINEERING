# we have to print this 
# *
# **
# ***
# ****
# *****
# ******
n=int(input("please enter the number upto which you want to make the pattern:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()