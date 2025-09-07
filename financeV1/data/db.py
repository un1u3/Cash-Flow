import sqlite3 
from models.transaction import Transaction, Income, Expense

DB_FILE = "finance.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            amount TEXT NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            note TEXT
        )
    ''')
    conn.commit()
    conn.close()


def add_trasaction(tx):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (type, amount, category, date, note) VALUES (?, ?, ?, ?, ?)",
        (tx.__class__.__name__, str(tx.amount), tx.category, tx.date.strftime("%Y-%m-%d"), tx.note)
    )
    conn.commit()
    conn.close()


def get_transactions():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, type, amount, category, date, note FROM transactions ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_transaction(tx_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id=?", (tx_id,))
    conn.commit()
    conn.close()

