from datetime import datetime

class Transaction:
    def __init__(self, transaction_type, amount):
        self._timestamp = datetime.now()
        self._transaction_type = transaction_type
        self._amount = amount

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def transaction_type(self):
        return self._transaction_type

    @property
    def amount(self):
        return self._amount

    # @amount.setter
    # def amount(self, new_amount):
    #     if new_amount >= 0:
    #         self._amount = new_amount
    #     else:
    #         raise ValueError("Amount must be non-negative.")
