def read_db(direction="db\credit_account.txt"):
    credit = open(direction, "r")
    credit_read = credit.read()
    credit.close
    return credit_read

def overwrite_database(direction="db\credit_account.txt"):
    credit = open(direction, "w")
    credit.write(input("Introduce the credit of the account: "))
    credit.close

def enter_credit(credit_account, credit_to_introduce, direction="db\credit_account.txt"):
    credit = open(direction, "w")
    credit.write(str(int(credit_to_introduce) + int(credit_account)))
    credit.close
    
def withdraw_credit(credit_account, credit_to_withdraw, direction="db\credit_account.txt"):
    credit = open(direction, "w")
    credit.write(str(int(credit_account) - int(credit_to_withdraw) ))
    credit.close