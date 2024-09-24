import sqlite3
def get_user_id(username):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    conn.close()
    
    return result[0] if result else None

def add_transaction(t_type,username,amount,description,date):
    
    transaction_type = t_type
    if transaction_type=="income":
        # username=input("Enter Your User Name:")
        user_id=get_user_id(username)
        # amount = float(input("Enter amount: "))
        # description = input("Enter description: ")
        # date = input("Enter date (YYYY-MM-DD): ")

        conn=sqlite3.connect('finance_manager.db')
        c=conn.cursor()
        c.execute('''
            INSERT INTO income (user_id,amount, description, date) 
            VALUES (?, ?, ?,?)''', (user_id,amount, description, date))
        conn.commit()
        print(f"{transaction_type.capitalize()} added successfully!")
    elif transaction_type=="expense":
        user_id=get_user_id(username)
        # amount = float(input("Enter amount: "))
        # description = input("Enter description: ")
        # date = input("Enter date (YYYY-MM-DD): ")

        conn=sqlite3.connect('finance_manager.db')
        c=conn.cursor()
        c.execute('''
            INSERT INTO expenses (user_id,amount, description, date) 
            VALUES (?, ?, ?,?)''', (user_id,amount, description, date))
        conn.commit()
        print(f"{transaction_type.capitalize()} added successfully!")

    else:
        print("Enter Valid Input")

def edit_transaction():
    transaction_type = input("Enter Update type (income/expense): ")
    if transaction_type=="income":
        username=get_user_id(username)
        income_id=input("Enter input id : ")
        amount=float(input("Enter New Amount : "))
        description=input("Enter New Description : ")
        date=input("Enter New Date (YYYY-MM-DD): ")
        with sqlite3.connect('finance_manager.db') as conn:
            c=conn.cursor()
            c.execute("UPDATE income SET amount = ?, description = ?, date = ? WHERE id = ?,user_id =?",
                   (amount, description, date, income_id,username))
        conn.commit()
        print(f"{transaction_type.capitalize()} update successfully!")

    elif transaction_type=="expense":
        expense_id=input("Enter input id : ")
        amount=float(input("Enter New Amount : "))
        description=input("Enter New Description : ")
        date=input("Enter New Date (YYYY-MM-DD): ")
        with sqlite3.connect('finance_manager.db') as conn:
            c=conn.cursor()
            c.execute("UPDATE expenses SET amount = ?, description = ?, date = ? WHERE id = ?",
                   (amount, description, date, expense_id))
        conn.commit()
        print(f"{transaction_type.capitalize()} update successfully!")

    else:
        print("Enter Valid Input")

def delete_transaction():
    table_name = input("Enter You Want To Delete (income/expenses): ")
    if table_name=="income":
        income_id=input("Enter Income id you want to delete :")
        conn = sqlite3.connect('finance_manager.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM income WHERE id = ?", (income_id,))
        conn.commit()
        # conn.close()
        print(f"{table_name.capitalize()} delete successfully!")

    elif table_name=="expenses":
        expense_id=input("Enter Expense id you want to delete :")
        conn = sqlite3.connect('finance_manager.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        # conn.close()
        print(f"{table_name.capitalize()} delete successfully!")

    else:
        print("Enter Valid Input")

# add_transaction()
# edit_transaction()
# delete_table()

def show_transaction(username):
    conn=sqlite3.connect("finance_manager.db")
    c=conn.cursor()
    data=input("What Do You Want To See (income/expense) :")
    if data=="income":
        user_id=get_user_id(username)
        c.execute('SELECT * FROM income where user_id = ?',(user_id,))
        rows = c.fetchall()

        if rows:  # Check if there are any rows returned
            for row in rows:
                print(row)
        else:
            print("No data found.")
    elif data=="expense":
        c.execute('SELECT * FROM expenses')
        rows = c.fetchall()

        if rows:  # Check if there are any rows returned
            for row in rows:
                print(row)
        else:
            print("No data found.")
    else:
        print("Enter Valid Input")
    
# show_transaction()
