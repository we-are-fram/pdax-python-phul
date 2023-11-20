from Domain.Transaction import Transaction
from datetime import datetime
import threading

class Account:
    def __init__(self, account_id, customer_id, account_number, balance=0):
        self._account_id = account_id
        self._customer_id = customer_id
        self._account_number = account_number
        self._balance = balance
        self._transactions = []  # A list to store transaction history
        self._lock = threading.Lock()  # Create a lock for synchronization

    @property
    def account_id(self):
        return self._account_id
    
    @property
    def customer_id(self):
        return self._customer_id
    
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def transactions(self):
        return self._transactions

    def deposit(self, amount):
        if amount > 0:
            with self._lock:
                self._balance += amount
                transaction = Transaction('deposit', amount)
                self._transactions.append(transaction)
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            with self._lock:
                self._balance -= amount
                transaction = Transaction('withdraw', amount)
                self._transactions.append(transaction)
            return True
        return False

    def get_balance(self):
        with self._lock:
            return self._balance
