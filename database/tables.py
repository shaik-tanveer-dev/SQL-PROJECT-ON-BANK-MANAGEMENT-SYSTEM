
from database.connection import DatabaseConfig

# table creation function
def createTables():
    db_config = DatabaseConfig()
    # cursor object creation
    cursor = db_config.cursor()

    # tables query
    

    user_table_query = """CREATE TABLE IF NOT EXISTS USERS(
                        ACCOUNT INT UNSIGNED AUTO_INCREMENT,
                        PASSWORD VARCHAR(30) NOT NULL, 
                        USERNAME VARCHAR(50) NOT NULL,
                        EMAIL VARCHAR(50) NOT NULL UNIQUE,
                        BALANCE INT UNSIGNED NOT NULL,
                        CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        PRIMARY KEY(ACCOUNT)
                    );"""

    Transactions_table_query = """CREATE TABLE IF NOT EXISTS TRANSACTIONS(
                                TRANSACTIONID INT UNSIGNED AUTO_INCREMENT,
                                ACCOUNT INT unsigned, 
                                TRANSACTIONTYPE ENUM('DEBIT', 'CREDIT'),
                                AMOUNT INT NOT NULL,
                                CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                PRIMARY KEY(TRANSACTIONID),
                                FOREIGN KEY(ACCOUNT) REFERENCES USERS(ACCOUNT)
                            );"""

    cursor.execute(user_table_query)
    cursor.execute(Transactions_table_query)

    db_config.commit()
    cursor.close()
    db_config.close()

    