# import manager

# print(manager.rohit_id)
# print(manager.rohit_pass)
# print(manager.eployee_list)
# # calling 
# manager.rohit_hii()
import manager as mng #naming the manager as mng which 
# can be used for further callling aand all

# print(mng.rohit_id)
# print(mng.rohit_pass)
# print(mng.eployee_list)
# print(mng.manager_address)
# print(mng.manager_name)
# print(mng.manager_pass)
# print()
# mng.rohit_hii()
# print()
# mng.manager_hii()
# ................some important point....................
# ........for importing specific data from another file we use.....
#  this below is the approach for that
from manager import rohit_id
from manager import rohit_pass
from manager import rohit_hii
print(rohit_id)
print(rohit_pass)
print()
rohit_hii()
# print(manager_id).....NameError: name 'manager_id' is not defined becoz
# manager_id is not imported into this file
from manager import manager_id
print(manager_id)# here we can access manager_id because we imported it here
#  ......................restricting specific data...................
# if this if statement is used then we cannot access 
# the data which is pst in it.

# if __name__=="__main__":>>>>>>>>>>>>>>this says that we this if block can be runned 
# or accessed in  main file only i.e.manager.py


    # def manager_hii():
    #     print("Manager name : ","Dharmpal")
    #     print('Dharmpal id : ',manager_id)
    #     print('Dharmpal password : ',manager_pass)

    #     manager_id = 'manager_boss@gmail.com'
    #     manager_pass = 'boss123456'

