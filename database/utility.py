from database.connection import DatabaseConfig


# add new user
def newUserDB(username:str, email:str, password:str, amount:int):
    db_config = DatabaseConfig()
    cursor = db_config.cursor()

    # check user exists or not
    cursor.execute("select 1 from users where email = %s;",(email,))
    if not cursor.fetchone():
        add_use_query = "INSERT INTO USERS" \
        "(USERNAME, EMAIL, PASSWORD,BALANCE) VALUES(%s, %s, %s, %s);"
        cursor.execute(add_use_query, (username, email, password, amount))

        # account no.query 
        cursor.execute("select account from users where email = %s;",(email,))
        account_no = cursor.fetchone()[0]
        db_config.commit()
        cursor.close()
        db_config.close()
        return f"Your accoun number is {account_no}"
    else:
        cursor.close()
        db_config.close()
        return "User email already exists"
    


# check login user
def checkLoginDB(account:int, password:str)->bool:
    db_config = DatabaseConfig()
    cursor = db_config.cursor()
    account_password_query = """SELECT PASSWORD FROM USERS
                                WHERE ACCOUNT = %s;"""
    cursor.execute(account_password_query,(account,))
    data= cursor.fetchone()
    
    if data:
        if data[0] == password:
            cursor.close()
            db_config.close()
            return True
    cursor.close()
    db_config.close()
    return False


# getbalance
def getBalanceDB(account:int):
    db_config = DatabaseConfig()
    cursor = db_config.cursor()
    get_balance_query = "SELECT BALANCE FROM USERS WHERE ACCOUNT = %s;"
    cursor.execute(get_balance_query,(account,))
    amount = cursor.fetchone()
    print(amount)
    db_config.close()
    cursor.close()
    if amount:
        return f"Current balance is: {amount[0]}"
    else:
        return "Current balance is: 0"

# add record to transactions table 
def addRecordToTransactions(account:int,trans_amount:int, trans_type:str="DEBIT"):
    db_config = DatabaseConfig()
    cursor = db_config.cursor()
    try:
        insert_trans_record = """
                INSERT INTO TRANSACTIONS(ACCOUNT, TRANSACTIONTYPE,AMOUNT)
                VALUES(%s, %s, %s);"""
        cursor.execute(insert_trans_record, (account, trans_type, trans_amount))
        db_config.commit()
        return True, 1
    except Exception as e:
        return False, e
    finally:
        cursor.close()
        db_config.close()



# withdraw function 
def withdrawDB(account:int, withdraw_amount:int):
    db_config = DatabaseConfig()
    cursor = db_config.cursor()
    try:
        get_balance_query = "SELECT BALANCE FROM USERS WHERE ACCOUNT = %s;"
        cursor.execute(get_balance_query,(account,))
        curr_amount = cursor.fetchone()[0]
        # check amount is sufficient
        if curr_amount >= withdraw_amount:
            # update in database
            updated_amount = curr_amount - withdraw_amount
            update_amount_query = "UPDATE USERS SET BALANCE = %s WHERE ACCOUNT = %s;"
            cursor.execute(update_amount_query,(updated_amount, account))
            # add transaction in transactions table
            insert_trans_record = """
                INSERT INTO TRANSACTIONS(ACCOUNT, TRANSACTIONTYPE,AMOUNT)
                VALUES(%s, %s, %s);"""
            cursor.execute(insert_trans_record, (account, "DEBIT", withdraw_amount))
            # commit database
            db_config.commit()
            return f"Withdraw successful and current balance is {updated_amount}"
        else:
            return "Insufficient Balance"
    except Exception as e:
        return f"Something wrong in database/utility.py - withdraw(): {e}"
    finally:
        
        db_config.close()
        cursor.close()


# withdraw function 
def depositeDB(account:int, deposite_amount:int):
    db_config = DatabaseConfig()
    cursor = db_config.cursor()
    try:
        get_balance_query = "SELECT BALANCE FROM USERS WHERE ACCOUNT = %s;"
        cursor.execute(get_balance_query,(account,))
        curr_amount = cursor.fetchone()[0]
        # check amount is sufficient
        if deposite_amount > 0:
            # update in database
            updated_amount = curr_amount + deposite_amount
            update_amount_query = "UPDATE USERS SET BALANCE = %s WHERE ACCOUNT = %s;"
            cursor.execute(update_amount_query,(updated_amount, account))
            # add transaction in transactions table
            insert_trans_record = """
                INSERT INTO TRANSACTIONS(ACCOUNT, TRANSACTIONTYPE,AMOUNT)
                VALUES(%s, %s, %s);"""
            cursor.execute(insert_trans_record, (account, "CREDIT", deposite_amount))
            # commit database
            db_config.commit()
            return f"Depsoite successful and current balance is {updated_amount}"
        else:
            return "Invalid Deposite amount"
    except Exception as e:
        return f"Something wrong in database/utility.py - deposite(): {e}"
    finally:
        
        db_config.close()
        cursor.close()

# Transfer
# withdraw function 
def TransferDB(from_acc:int,to_acc:int, transfer_amount:int):
    db_config = DatabaseConfig()
    cursor = db_config.cursor()
    try:
        get_balance_query = "SELECT BALANCE FROM USERS WHERE ACCOUNT = %s;"
        cursor.execute(get_balance_query,(from_acc,))
        from_curr_amount = cursor.fetchone()[0]
        
        # check amount is sufficient
        cursor.execute("select 1 from users where account = %s;",(to_acc,))
        
        if from_curr_amount >= transfer_amount and cursor.fetchone():
            cursor.execute(get_balance_query,(to_acc,))
            to_curr_amount = cursor.fetchone()[0]
            # update in database in from account
            from_updated_amount = from_curr_amount - transfer_amount
            update_amount_query = "UPDATE USERS SET BALANCE = %s WHERE ACCOUNT = %s;"
            cursor.execute(update_amount_query,(from_updated_amount, from_acc))

            # update in database in from account in to_account
            to_updated_amount = to_curr_amount + transfer_amount
            update_amount_query = "UPDATE USERS SET BALANCE = %s WHERE ACCOUNT = %s;"
            cursor.execute(update_amount_query,(to_updated_amount, to_acc))
            # add transaction in transactions table
            insert_trans_record = """
                INSERT INTO TRANSACTIONS(ACCOUNT, TRANSACTIONTYPE,AMOUNT)
                VALUES(%s, %s, %s);"""
            cursor.execute(insert_trans_record, (from_acc, "DEBIT", transfer_amount))

            # add credit transactions
            insert_trans_record = """
                INSERT INTO TRANSACTIONS(ACCOUNT, TRANSACTIONTYPE,AMOUNT)
                VALUES(%s, %s, %s);"""
            cursor.execute(insert_trans_record, (to_acc, "CREDIT", transfer_amount))
            # commit database
            db_config.commit()
            return f"Transfer successful and current balance is {from_updated_amount}"
        else:
            return "Insufficient Balance"
    except Exception as e:
        return f"Something wrong in database/utility.py - withdraw(): {e}"
    finally:
        
        db_config.close()
        cursor.close()


# withdraw function 
def ministatementDB(account:int):
    db_config = DatabaseConfig()
    cursor = db_config.cursor()
    cursor.execute("SELECT * FROM TRANSACTIONS WHERE ACCOUNT = %s;",(account,))
    transactions = cursor.fetchall()
    if transactions:
        return transactions
    else:
        return "No Transactions Found"
