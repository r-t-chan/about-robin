def connectDatabaseUserSpec():
    import psycopg2
    strUser = input("\nPlease enter the Username required to connect into the lab5 database:\n") #authenticate user
    strPassword = input("\nPassword:\n")
    strDatabase = input("\nPlease enter the database you would like to connect to:\n")
    strHost = input("\nPlease enter the host address you would like to connect to:\n")
    strPort = input("\nPlease enter the port number you would like to connect to:\n")
    conn = psycopg2.connect(user=strUser, password=strPassword, database=strDatabase, host=strHost, port=strPort)
    print("\n###Successfully connected!!###\n")
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT VERSION();") #find version
    db_version = cursor.fetchone()
    print(db_version)
    cursor.execute("CREATE TABLE psycopg_tbl(id SERIAL PRIMARY KEY, str_col VARCHAR(50),int_col INT);") #add table
    print("Table successfully created!")  
    cursor.execute("INSERT INTO psycopg_tbl(str_col, int_col) VALUES('Hello Scott!', 420);") #add value to table
    conn.commit()
    print("Value added to table!")
    conn.close()

connectDatabaseUserSpec()
