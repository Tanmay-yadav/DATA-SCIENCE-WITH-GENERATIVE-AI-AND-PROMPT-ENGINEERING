manager_name = "Dharmpal ji"
manager_address = "Bihar"

eployee_list = ['rohit','rahul','mohit','suresh','jagdessh'] 

rohit_id = 'hello@gmail.com'
rohit_pass = "124@786"

def rohit_hii():
    print("Employee name : ","Rohit")
    print('Rohit id : ',rohit_id)
    print('ROhit password : ',rohit_pass)
if __name__=="__main__":#restriction code but
    #if we use "manager" instead of "__main__"
    # then it can be accessed again  

    def manager_hii():
        print("Manager name : ","Dharmpal")
        print('Dharmpal id : ',manager_id)
        print('Dharmpal password : ',manager_pass)

        manager_id = 'manager_boss@gmail.com'
        manager_pass = 'boss123456'
