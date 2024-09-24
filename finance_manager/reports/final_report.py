import sqlite3
from datetime import datetime

def generate_final_report(username):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()

    # Retrieve user_id based on the provided username
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    if not user:
        print("User not found.")
        return

    user_id = user[0]

    cursor.execute("SELECT amount, description, date FROM income WHERE user_id = ?", (user_id,))
    income_data = cursor.fetchall()

    cursor.execute("SELECT amount, description, date FROM expenses WHERE user_id = ?", (user_id,))
    expenses_data = cursor.fetchall()

    total_income = sum([income[0] for income in income_data])
    total_expenses = sum([expense[0] for expense in expenses_data])
    balance = total_income - total_expenses
    
    report = f"Final Financial Report for {username}\n"
    report += "=" * 50 + "\n"
    report += "Income:\n"
    for income in income_data:
        report += f"- {income[1]}: {income[0]} on {income[2]}\n"
    report += f"Total Income: {total_income}\n\n"

    report += "Expenses:\n"
    for expense in expenses_data:
        report += f"- {expense[1]}: {expense[0]} on {expense[2]}\n"
    report += f"Total Expenses: {total_expenses}\n\n"

    report += "=" * 50 + "\n"
    report += f"Balance: {balance}\n"
    report += "=" * 50 + "\n"
    report += f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    
    conn.close()

    return report


# Example usage
# username = "sikander"  # Replace with the actual username
# report = generate_final_report(username)
# print(report)
