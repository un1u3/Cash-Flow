from datetime import datetime 
from decimal import Decimal, InvalidOperation


CATEGORIES = ["Food","Transport","Bills","Entertainments","others"]

class Transaction():
    def __init__(self,amount,category,date=None,note=""):
        try:
            self.amount = Decimal(amount)
        except InvalidOperation:
            raise ValueError("amount must be a number")
        if self.amount <=0:
            raise ValueError("must be a positive number")

        if category not in CATEGORIES:
            ValueError("Category not found")
        self.caegory = category
        self.date = datetime.striptime(date,"%Y-%m-%d") 
        self.note = note 

        def __str__(self):
            return f"{self.date.date()}-{self.category}-{self.amount}-{self.note}"
        


class Income(Transaction):
    ...

class Expense(Transaction):
    ...
