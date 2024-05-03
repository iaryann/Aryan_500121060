# -*- coding: utf-8 -*-

import datetime

def load_transactions(file_name):
    """
    Load transactions from a file.
    """
    transactions = []
    with open(file_name, 'r') as file:
        for line in file:
            transaction = eval(line)
            transactions.append(transaction)
    return transactions

def save_transactions(transactions, file_name):
    """
    Save transactions to a file.
    """
    with open(file_name, 'w') as file:
        for transaction in transactions:
            file.write(str(transaction) + '\n')

def addtransaction(transactions, description, amount, category, date=None):
    """
    Add a new transaction to the list of transactions.
    If no date is provided, use today's date. 
    Returns the updated list of transactions.
    """
    transaction = {
        "description": description,
        "amount": amount,
        "category": category,
        "date": date or datetime.datetime.today().strftime("%Y-%m-%d")
    }
    transactions.append(transaction)
    return transactions

def removetransaction(transactions, index):
    """
    Remove a transaction from the list of transactions by index.
    Returns the amount of the removed transaction and the updated list of transactions.
    """
    transaction = transactions.pop(index)
    return transaction["amount"], transactions

def displaytransactions(transactions):
    """
    Display the list of transactions.
    """
    for i, transaction in enumerate(transactions):
        print(f"{i + 1}. {transaction['description']}: {transaction['amount']} ({transaction['category']} - {transaction['date']})")

def get_transactions_category(transactions, category):
    """
    Return a list of all transactions that belong to a given category.
    """
    return [t for t in transactions if t["category"] == category]

def get_transactions_date(transactions, date):
    """
    Return a list of all transactions that took place on a given date.
    """
    return [t for t in transactions if t["date"] == date]

def get_balance_category(transactions, category):
    """
    Return the total balance for all transactions in a given category.
    """
    filtered_transactions = get_transactions_category(transactions, category)
    return sum(t["amount"] for t in filtered_transactions)

def get_spending_date(transactions, date):
    """
    Return the total spending on a given date.
    """
    filtered_transactions = get_transactions_date(transactions, date)
    return sum(t["amount"] for t in filtered_transactions)

def main():
    """
    The main function that runs the transaction tracking program.
    """
    transactions = []
    balance = 0
    file_name = 'transactions.txt'
    transactions = load_transactions(file_name)
    balance = sum(t['amount'] for t in transactions)

    while True:
        #... the rest of the main function...

     save_transactions(transactions, file_name)

    while True:
        print("\n1. Add transaction")
        print("2. Remove transaction")
        print("3. Display transactions")
        print("4. Get balance by category")
        print("5. Get spending by date")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            description = input("Enter transaction description: ")
            amount = float(input("Enter transaction amount: "))
            category = input("Enter transaction category: ")
            date = input("Enter transaction date (YYYY-MM-DD, optional): ") or None
            transactions = addtransaction(transactions, description, amount, category, date)
            balance += amount
            print("Transaction added successfully")
        elif choice == 2:
            index = int(input("Enter index of transaction to remove: "))
            amount_removed, transactions = removetransaction(transactions, index - 1)
            balance -= amount_removed
            print("Transaction removed successfully")
        elif choice == 3:
            displaytransactions(transactions)
            print(f"\nTotal balance: {balance}")
        elif choice == 4:
            category = input("Enter category: ")
            category_balance = get_balance_category(transactions, category)
            print(f"Balance for {category}: {category_balance}")
        elif choice == 5:
            date = input("Enter date (YYYY-MM-DD): ")
            daily_spending = get_spending_date(transactions, date)
            print(f"Spending on {date}: {daily_spending}")
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")


main()