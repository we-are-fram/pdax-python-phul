class AccountRepository:
    def __init__(self):
        # In-memory storage for accounts, using a dictionary
        self.accounts = {}

    def save_account(self, account):
        # Save the account using account_id as the key
        self.accounts[account.account_id] = account

    def find_account_by_id(self, account_id):
        # Retrieve an account by its ID
        return self.accounts.get(account_id)

    def find_accounts_by_customer_id(self, customer_id):
        # Retrieve all accounts associated with a customer ID
        return [account for account_id, account in self.accounts.items() if account.customer_id == customer_id]

