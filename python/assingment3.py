# write a program to find out the minimum item in list without using predefined
#  min or max function
mylist=[1,45,66,79,98,99,0,-1,-2,-77]
print(mylist)
# minimum= mylist[0]


# for item in mylist:
    
#     if item<minimum:
#         minimum = item

# print("the minimum number is",minimum)            
          
maximum =mylist[0]        

for i in range(10):
    if maximum< mylist[i]:
        maximum = mylist[i]

print("the maximum number is ",maximum)
          

        



