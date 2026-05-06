
# imporrt necessry modules
# from database.tables import createTables
from database import createTables
from database import newUserDB, checkLoginDB, getBalanceDB, withdrawDB, depositeDB
from database import ministatementDB, TransferDB
#operations
def login(account:int, password:str)->bool:
    return checkLoginDB(account=account, password=password)
        

def register(username:str,email:str,password:str, deposite_amount:int):
    # call newUser function
    return newUserDB(username=username,
                   email=email,
                   password=password,
                   amount=deposite_amount)
    
    

def get_balance(account:int)->int:
    return getBalanceDB(account=account)

def withdraw(account:int, withdraw_amount:int)->str:
    return withdrawDB(account=account, withdraw_amount=withdraw_amount)


def deposite(account:int, deposite_amount:int)->str:
    return depositeDB(account=account, deposite_amount=deposite_amount)

def transfer(from_account:int, to_account:int, transfer_amount):
    return TransferDB(from_acc=from_account,
                      to_acc=to_account,
                      transfer_amount=transfer_amount)

def ministatement(account:int)->list[dict]:
    return ministatementDB(account=account)

def logout():
    exit()
    



# main
if __name__ == "__main__":
    createTables()
    print("Welcome to the small scale bank")
    print("Select your operation \n 1. Register \n 2. Login")
    choice = int(input("Enter your operation number:"))
    if choice == 1:
        username = input("Enter username:")
        email = input("Enter email id:")
        initial_deposite = int(input("Enter your initial deposite amount:"))
        password = input("Enter password:")

        # call register function
        print(register(username=username,
                       email=email,
                       password=password,
                       deposite_amount=initial_deposite))

    elif choice == 2:
        account_no = int(input("Enter your account number:"))
        password = input("Enter your password:")
        # call login function
        login_val = login(account=account_no, password=password)
        while login_val:
            print("Select Your operation \n 1. Get Balance \n 2. Withdraw \n" 
            " 3. Deposite \n 4. Transfer \n 5. Mini statement \n 6. Logout")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                print(get_balance(account=account_no))

            elif choice == 2:
                amount = int(input("Enter withdraw amount:"))
                print(withdraw(account=account_no, withdraw_amount=amount))

            elif choice == 3:
                amount = int(input("Enter deposite amount:"))
                print(deposite(account=account_no, deposite_amount=amount))
            elif choice == 4:
                to_account= int(input("Enter reciever account number:"))
                amount = int(input("Enter transfer amount:"))
                print(transfer(from_account=account_no, 
                               to_account=to_account,
                               transfer_amount=amount))
            elif choice == 5:
                print(ministatement(account=account_no))
            elif choice == 6:
                print("Thak you, Bye bye....")
                exit()
        if login_val == False:
            print("Invalid credentials")

         