#  _______________________ASSINGMENT FOR TODAY___________________________________
# .............................................................................
# 1.average_finder()
#2. even_finder()
# 3.average_finder_even()
# 4.my_min()
# 5.my_max()
#.............................................................
marks =[10,2,3,4,77,88,97,0,54]
# __________________1.average finder______________________________
# def average_finder(list):
#     count=0
#     for item in list:
#         count+=item
#     return count    

# print("average is:",average_finder(marks)/len(marks))
# _________________________________________________________________
# ________________________2.even finder______________________________
# def even_finder(list):
#     count=0
#     for item in list:
#         if item%2==0 and item!=0:
#             count+=1
#     return count    
# output=even_finder(marks)
# print("the number of even in the list are:",output)
# _______________________________________________________________________
# # _________________________3.average_finder_even___________________________
# def average_finder_even(list):
    
    
#     even_sum=0
#     for item in list:
#         if item%2==0 and item!=0:
#             even_sum+=item
            
#     return even_sum 
# def even_finder2(list):
#     count=0
#     for item in list:
#         if item%2==0 and item!=0:
#             count+=1
#     return count    
# output2=even_finder2(marks)
# output =average_finder_even(marks)/output2
# print("the average  of even numbers present is: ",output)       
# ..........................................................
# # ______________________4.my_min____________________________
# def my_min(list):
#     minimum=list[0]
#     for item in list:
       
#        if item<minimum:
#            minimum=item
#     return minimum
               
# output=my_min(marks)
# print("the minimum number is:",output)               
# ........................................................................
# _________________________5.my_max_______________________________________
def my_max(list):
    maximum =list[0]
    for item in list:
        if item>maximum:
            maximum=item
    return maximum
print("the maximum number is:",my_max(marks))        
# ..........................................................................
# __________________________________________________________________________