from libs.uiInterface import user_interface
from libs.dbOperations import read_db
from libs.dbOperations import overwrite_database
from libs.dbOperations import enter_credit
from libs.dbOperations import withdraw_credit


while True is True:
    try:
        option = int(user_interface())
    
        if option == 1:
            print(read_db())
    
        elif option == 2:
            overwrite_database()
    
        elif option == 3:
            enter_credit(credit_account=read_db(), credit_to_introduce=int(input("Enter the credit to aggregate: ")))
    
        elif option == 4:
            withdraw_credit(credit_account=read_db(), credit_to_withdraw=int(input("Enter the credit to withdraw: ")))
    
        elif option == 5:
            break
    
        else:
            print("Invalid option")
    except ValueError:
        print("Invalid value")