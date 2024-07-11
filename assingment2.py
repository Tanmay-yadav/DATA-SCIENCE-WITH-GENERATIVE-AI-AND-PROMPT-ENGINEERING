# we have to print this
# 1
# 12
# 123
# 1234
# 12345

n=int(input("please enter the number upto which you want to make the pattern:"))
for i in range(1,n+1):
    for j in range(1,i+1):#start=1,end=i+1
        print(j,end="")# the print("*", end="") prints asterisk characters on 
        # the same line, while the print() statement with no arguments prints a 
        # newline, moving to the next line for the next set of asterisks.
    print() #this add new line after inner loop