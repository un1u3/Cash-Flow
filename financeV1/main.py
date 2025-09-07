from data.db import init_db, add_transaction, get_transactions, delete_transaction
from models.transaction import Income, Expense, CATEGORIES

def main():
    init_db()
    print("Welcome to Personal Finance Dashboard v1")

    while True:
        print("\nOptions: [1] Add [2] View [3] Delete [0] Exit")
        choice = input("Choose: ")

        if choice == "1":
            type_ = input("Type (Income/Expense): ")
            amount = input("Amount: ")
            category = input(f"Category {CATEGORIES}: ")
            note = input("Note (optional): ")

            try:
                tx = Income(amount, category) if type_ == "Income" else Expense(amount, category)
                tx.note = note
                add_transaction(tx)
                print("✅ Transaction added!")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            rows = get_transactions()
            print("\nID | Type | Amount | Category | Date | Note")
            for r in rows:
                print(r)

        elif choice == "3":
            tx_id = input("Transaction ID to delete: ")
            delete_transaction(tx_id)
            print("🗑 Transaction deleted!")

        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
