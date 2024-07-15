name=(input("plz enter your name"))
print("hello",name)
message="""
type1>>>>check balance
type2>>>>withdrawl
type3>>>>deposit
"""
print(message)
task =int(input("plz enter the number:"))
if task >=1 and task<=3:
    print("welcome to the bank")
    available_balance=5000
    if task==1:
        print("the available balance is:",available_balance)   

    elif task==2:
        withdrawl_amount=int(input("plz enter the withdrawl amount:"))
        if withdrawl_amount>available_balance:
            print("insufficient amount")  
            print("the available amount is:",available_balance)
        elif withdrawl_amount<=available_balance:
            print(withdrawl_amount)
            available_balance=available_balance-withdrawl_amount

            print("current balance:",available_balance)
    else:
        deposit_amount=int(input("plz enter the deposit amount"))
        if deposit_amount>=1:
            print("available balance in account",available_balance)
            available_balance=available_balance+deposit_amount

            print("the amount:",deposit_amount,"is succefully deposited") 
                         
            print("current balance after deposition",available_balance)
else:
    print("plz input the correct number")        