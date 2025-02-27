from libs.dbOperations import read_db
from libs.dbOperations import overwrite_database

def user_interface():
    print("------Banking Sistem------")
    if read_db() == "":
        overwrite_database()
        option = 0
    else:
        print("1-Show credit")
        print("2-Change credit")
        print("3-Enter credit")
        print("4-Withdraw credit")
        print("5-Exit")
        option = int(input("Chose a option: "))
    
    return option
    