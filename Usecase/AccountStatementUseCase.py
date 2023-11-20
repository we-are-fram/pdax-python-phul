class AccountStatementUseCase:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def generate_account_statement(self, account_id):
        account = self.account_repository.find_account_by_id(account_id)
        if account is None:
            return "Account not found"

        statement = f"Account Statement for {account_id}\n"
        statement += f"Account Number: {account.account_number}\n"
        statement += f"Balance: {account.get_balance()}\n"
        statement += "Transactions:\n"

        for transaction in account.transactions:
            timestamp, trans_type, amount = transaction.timestamp, transaction.transaction_type, transaction.amount
            statement += f"{timestamp} - {trans_type.capitalize()} - Amount: {amount}\n"

        return statement