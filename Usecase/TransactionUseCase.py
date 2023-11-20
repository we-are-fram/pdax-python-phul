class TransactionUseCase:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def make_transaction(self, account_id, amount, transaction_type):
        account = self.account_repository.find_account_by_id(account_id)

        if account is None:
            raise ValueError("Account not found")

        if transaction_type == 'deposit':
            if not account.deposit(amount):
                raise ValueError("Invalid deposit amount")
        elif transaction_type == 'withdraw':
            if not account.withdraw(amount):
                raise ValueError("Insufficient funds for withdrawal")
        else:
            raise ValueError("Invalid transaction type")

        # Additional logic for recording the transaction can be added here

        # Update the account in the repository
        self.account_repository.save_account(account)